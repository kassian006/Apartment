from tokenize import TokenError
from rest_framework import viewsets, generics, status, permissions, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .filters import HouseFilter, AgentProfileFilter, ResumeListFilter, AgentRatingFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework import filters
from django_filters import rest_framework as django_filters
from .paginations import *
from .serializers import *
from .models import *
from .permissions import CheckUser
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail':' неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)
        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'detail': 'Refresh токен не предоставлен.'}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Вы успешно вышли.'}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({'detail': 'Недействительный токен.'}, status=status.HTTP_400_BAD_REQUEST)


class AgentRegisterView(generics.CreateAPIView):
    serializer_class = AgentUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AgentCustomLoginView(TokenObtainPairView):
    serializer_class = AgentLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail':' неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)
        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class AgentLogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class HouseListAPIView(generics.ListAPIView):
    queryset = House.objects.filter(type_home="Buy")
    serializer_class = HouseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['location']
    filterset_class = HouseFilter
    ordering_fields = ['price', 'bedroom']
    pagination_class = HousePagination


class HouseCreateAPIView(generics.CreateAPIView):
    queryset = House.objects.filter(type_home="Buy")
    serializer_class = HouseCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        house = serializer.save(owner=user)  # Назначаем владельца дома

        # Если пользователь "клиент", делаем его "владельцем"
        if user.role == 'client':
            user.role = 'owner'
            user.save()


class HouseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter(type_home="Buy")
    serializer_class = HouseDetailSerializer


# -----------------------rent--------------------------------------


class HouseListRentAPIView(generics.ListAPIView):
    queryset = House.objects.filter(type_home="Rent")
    serializer_class = HouseListRentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['location']
    filterset_class = HouseFilter
    ordering_fields = ['price', 'bedroom']
    pagination_class = HousePagination


class HouseCreateRentAPIView(generics.CreateAPIView):
    queryset = House.objects.filter(type_home="Rent")
    serializer_class = HouseCreateRentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        house = serializer.save(owner=user)  # Назначаем владельца дома

        # Если пользователь "клиент", делаем его "владельцем"
        if user.role == 'client':
            user.role = 'owner'
            user.save()


class HouseRetrieveUpdateDestroyRentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter(type_home="Rent")
    serializer_class = HouseDetailRentSerializer


class RealtyApplicationListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = RealtyApplicationListSerializer
    permission_classes = [CheckUser]


class RealtyApplicationDetailRentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter(type_home="Rent")
    serializer_class = RealtyApplicationDetailSerializer
    permission_classes = [CheckUser]


class RealtyApplicationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter(type_home="Buy")
    serializer_class = RealtyApplicationDetailSerializer
    permission_classes = [CheckUser]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileEditSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class AgentProfileListAPIView(generics.ListAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AgentProfileFilter
    search_fields = ['first_name', 'last_name', 'username']
    pagination_class = HousePagination



class AgentProfileInfoAPIView(generics.ListAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileInfoSerializer


class AgentProfileTableAPIView(generics.ListAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileInfoSerializer
    pagination_class = HousePagination
    permission_classes = [CheckUser]


class AgentProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileDetailSerializer

    def get_queryset(self):
        return AgentProfile.objects.filter(id=self.request.user.id)



class ResumeListAPIView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeListSerializer
    filter_backends = [filters.SearchFilter, django_filters.DjangoFilterBackend]
    filterset_class = ResumeListFilter
    search_fields = ['agent__username']  # Поле для поиска
    permission_classes = [CheckUser]



class ResumeDetailAPIView(generics.RetrieveAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeDetailSerializer
    permission_classes = [CheckUser]


class AgentRatingAPIView(generics.ListAPIView):
    queryset = AgentRating.objects.all()
    serializer_class = AgentRatingSerializer
    filter_backends = [filters.SearchFilter, django_filters.DjangoFilterBackend]
    filterset_class = AgentRatingFilter
    search_fields = ['agent__username']
    permission_classes = [CheckUser]


class AgentRatingCreateAPIView(generics.CreateAPIView):
    serializer_class = AgentRatingSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            agent = serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({'detail': 'Маалымат туура эмес берилди'}, status.HTTP_400_BAD_REQUEST)
        except NameError as e:
            return Response({'detail': f'{e}, Ошибка в коде'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception:
            return Response({'detail': 'Сервер не работает'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class HouseReviewAPIView(generics.ListAPIView):
    queryset = HouseReview.objects.all()
    serializer_class = HouseReviewSerializer
    filter_backends = [filters.SearchFilter, django_filters.DjangoFilterBackend]
    search_fields = ['house__house_name']  # Поле для поиска


class HouseReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = HouseReviewCreateSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            agent = serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({'detail': 'Маалымат туура эмес берилди'}, status.HTTP_400_BAD_REQUEST)
        except NameError as e:
            return Response({'detail': f'{e}, Ошибка в коде'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception:
            return Response({'detail': 'Сервер не работает'}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class PublishedMessagesView(generics.ListAPIView):
    queryset = Message.objects.filter(status='published')
    serializer_class = MessageSerializer
    permission_classes = [CheckUser]


class AllMessagesView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [CheckUser]

    def get_queryset(self):
        queryset = Message.objects.all()
        status = self.request.query_params.get('status', None)
        is_read = self.request.query_params.get('is_read', None)
        if status:
            queryset = queryset.filter(status=status)
        if is_read is not None:
            queryset = queryset.filter(is_read=(is_read.lower() == 'true'))
        return queryset


class DeclinedMessagesView(generics.ListAPIView):
    queryset = Message.objects.filter(status='declined')
    serializer_class = MessageSerializer
    permission_classes = [CheckUser]

from rest_framework import viewsets, generics, status, permissions, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HouseFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from .paginations import *
from .serializers import *
from .models import *
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


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class HouseListAPIView(generics.ListAPIView):
    queryset = House.objects.filter(type_home="Buy")
    serializer_class = HouseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['location']
    filterset_class = HouseFilter
    ordering_fields = ['price']
    pagination_class = HousePagination


class HouseCreateAPIView(generics.CreateAPIView):
    queryset = House.objects.filter(type_home="Buy")
    serializer_class = HouseCreateSerializer


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
    ordering_fields = ['price']
    pagination_class = HousePagination


class HouseCreateRentAPIView(generics.CreateAPIView):
    queryset = House.objects.filter(type_home="Rent")
    serializer_class = HouseCreateRentSerializer


class HouseRetrieveUpdateDestroyRentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter(type_home="Rent")
    serializer_class = HouseDetailRentSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileEditSerializer


class AgentProfileListAPIView(generics.ListAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileListSerializer


class AgentProfileInfoAPIView(generics.ListAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileInfoSerializer


class AgentProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileDetailSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class AgentRatingViewSet(viewsets.ModelViewSet):
    queryset = AgentRating.objects.all()
    serializer_class = AgentRatingSerializer


class HouseReviewViewSet(viewsets.ModelViewSet):
    queryset = HouseReview.objects.all()
    serializer_class = HouseReviewSerializer

from rest_framework import viewsets, generics, status, permissions, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HouseFilter, AgentProfileFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from .paginations import *
from .serializers import *
from .models import *


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
    ordering_fields = ['price']
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


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileEditSerializer


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


class AgentProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileDetailSerializer


class ResumeListAPIView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeListSerializer


class ResumeDetailAPIView(generics.RetrieveAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeDetailSerializer


class AgentRatingAPIView(generics.ListAPIView):
    queryset = AgentRating.objects.all()
    serializer_class = AgentRatingSerializer


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


class HouseReviewViewSet(viewsets.ModelViewSet):
    queryset = HouseReview.objects.all()
    serializer_class = HouseReviewSerializer

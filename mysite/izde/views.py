from rest_framework import viewsets, generics, status, permissions, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HouseFilter
from rest_framework.filters import OrderingFilter, SearchFilter
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
    serializer_class = UserProfileSerializer


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

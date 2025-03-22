from rest_framework import viewsets, generics, status, permissions, serializers
from .models import (UserProfile, House, Category)
from .serializers import (UserProfileSimpleSerializer, HouseListSerializer, HouseCreateSerializer, HouseDetailSerializer, CategorySerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class HouseListAPIView(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseListSerializer


class HouseCreateAPIView(generics.CreateAPIView):
    serializer_class = HouseCreateSerializer


class HouseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, basename='categories')

urlpatterns = [
    path('house/', HouseListAPIView.as_view(), name='house_list'),
    path('house_create/', HouseCreateAPIView.as_view(), name='house_create'),
    path('house/<int:pk>/', HouseRetrieveUpdateDestroyAPIView.as_view(), name='house_detail'),
]
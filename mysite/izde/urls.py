from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, basename='categories')

urlpatterns = [
    path('house/', HouseListAPIView.as_view(), name='house_list'),
    path('house_create/', HouseCreateAPIView.as_view(), name='house_create'),
    path('house/<int:pk>/', HouseRetrieveUpdateDestroyAPIView.as_view(), name='house_detail'),

    # ----------------------------------rent-------------------------------------------

    path('house_rent/', HouseListRentAPIView.as_view(), name='house_rent_list'),
    path('house_rent_create/', HouseCreateRentAPIView.as_view(), name='house_rent_create'),
    path('house_rent/<int:pk>/', HouseRetrieveUpdateDestroyRentAPIView.as_view(), name='house_rent_detail'),
]

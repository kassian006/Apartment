from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'resume', ResumeViewSet, basename='resume'),
router.register(r'agent_rating', AgentRatingViewSet, basename='agent_rating'),
router.register(r'house_review', HouseReviewViewSet, basename='house_review'),

urlpatterns = [
    #------------------------client_register------------------------#
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    #------------------------agent_register--------------------------#
    path('agent_register/', AgentRegisterView.as_view(), name='agent_register'),
    path('agent_login/', AgentCustomLoginView.as_view(), name='agent_login'),
    path('agent_logout/', AgentLogoutView.as_view(), name='agent_logout'),


    path('', include(router.urls)),
    path('house/', HouseListAPIView.as_view(), name='house_list'),
    path('house_create/', HouseCreateAPIView.as_view(), name='house_create'),
    path('house/<int:pk>/', HouseRetrieveUpdateDestroyAPIView.as_view(), name='house_detail'),

    # ----------------------------------rent-------------------------------------------

    path('house_rent/', HouseListRentAPIView.as_view(), name='house_rent_list'),
    path('house_rent_create/', HouseCreateRentAPIView.as_view(), name='house_rent_create'),
    path('house_rent/<int:pk>/', HouseRetrieveUpdateDestroyRentAPIView.as_view(), name='house_rent_detail'),

    path('agent/', AgentProfileListAPIView.as_view(), name='agent'),
    path('agent/<int:pk>/', AgentProfileDetailAPIView.as_view(), name='agent'),
    path('agent_info/', AgentProfileInfoAPIView.as_view(), name='agent_info'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'resume', ResumeViewSet, basename='resume'),
router.register(r'agent_rating', AgentRatingViewSet, basename='agent_rating'),
router.register(r'house_review', HouseReviewViewSet, basename='house_review'),

urlpatterns = [
    path('', include(router.urls)),
    path('agent/', AgentProfileListAPIView.as_view(), name='agent'),
    path('agent/<int:pk>/', AgentProfileDetailAPIView.as_view(), name='agent'),
    path('agent_info/', AgentProfileInfoAPIView.as_view(), name='agent_info'),

]

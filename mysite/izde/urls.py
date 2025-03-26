from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),

urlpatterns = [
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

    path('resume/', ResumeListAPIView.as_view(), name='resume'),
    path('resume/<int:pk>/', ResumeDetailAPIView.as_view(), name='resume'),

    path('agent_rating/', AgentRatingAPIView.as_view(), name='agent_rating'),
    path('agent_rating/create/', AgentRatingCreateAPIView.as_view(), name='agent_rating_create'),

    path('house_review/', HouseReviewAPIView.as_view(), name='house_review'),
    path('house_review/create/', HouseReviewCreateAPIView.as_view(), name='house_review_create'),

]
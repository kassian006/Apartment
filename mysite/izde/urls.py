from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),

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
    path('password_reset/verify_code/', verify_reset_code, name='verify_reset_code'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('house/', HouseListAPIView.as_view(), name='house_list'),
    path('house_create/', HouseCreateAPIView.as_view(), name='house_create'),
    path('house/<int:pk>/', HouseRetrieveUpdateDestroyAPIView.as_view(), name='house_detail'),

    # ----------------------------------rent-------------------------------------------

    path('house_rent/', HouseListRentAPIView.as_view(), name='house_rent_list'),
    path('house_rent_create/', HouseCreateRentAPIView.as_view(), name='house_rent_create'),
    path('house_rent/<int:pk>/', HouseRetrieveUpdateDestroyRentAPIView.as_view(), name='house_rent_detail'),

    path('realty/', RealtyApplicationListAPIView.as_view(), name='realty-list'),
    path('realty_buy/<int:pk>/', RealtyApplicationDetailAPIView.as_view(), name='realty-buy-detail'),
    path('realty_rent/<int:pk>/', RealtyApplicationDetailRentAPIView.as_view(), name='realty-rent-detail'),

    path('agent/', AgentProfileListAPIView.as_view(), name='agent'),
    path('agent/<int:pk>/', AgentProfileDetailAPIView.as_view(), name='agent'),
    path('agent_info/', AgentProfileInfoAPIView.as_view(), name='agent_info'),
    path('agent_table/', AgentProfileTableAPIView.as_view(), name='agent_table'),

    path('resume/', ResumeListAPIView.as_view(), name='resume'),
    path('resume/<int:pk>/', ResumeDetailAPIView.as_view(), name='resume'),

    path('agent_rating/', AgentRatingAPIView.as_view(), name='agent_rating'),
    path('agent_rating/create/', AgentRatingCreateAPIView.as_view(), name='agent_rating_create'),

    path('house_review/', HouseReviewAPIView.as_view(), name='house_review'),
    path('house_review/create/', HouseReviewCreateAPIView.as_view(), name='house_review_create'),

    path('inbox1/', PublishedMessagesView.as_view(), name='inbox1'),
    path('inbox2/', AllMessagesView.as_view(), name='inbox2'),
    path('inbox3/', DeclinedMessagesView.as_view(), name='inbox3'),

]
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('hoods/', HoodCreateView.as_view(), name='hoods'),
    path('hood/<str:search_term>/', HoodDetailsView.as_view(), name='specifichood'),
    path('join/<str:hood_name>/<str:user_name>', UpdateHoodOptionJoinView.as_view(), name='joinhood'),
    path('admin/set/<str:hood_name>/<str:user_name>', UpdateHoodAdminView.as_view(), name='sethoodadmin'),
    path('profiles/', ProfileCreateView.as_view(), name='profiles'),
    path('profile/<str:user_name>/', ProfileDetailsView.as_view(), name='specificprofile'),
    path('posts/<str:filter_name>/', PostListCreateView.as_view(), name='posts'),
    path('bussinesses/<str:filter_name>/', BussinessListCreateView.as_view(), name='bussinesses'),
    path('services/<str:filter_name>/', EmergencyServiceListCreateView.as_view(), name='emergencyservice'),
]
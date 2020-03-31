from django.urls import path
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('hoods/', login_required(HoodCreateView.as_view()), name='hoods'),
    path('hood/<str:search_term>/', login_required(HoodDetailsView.as_view()), name='specifichood'),
    path('join/<str:hood_name>/<str:user_name>', login_required(UpdateHoodOptionJoinView.as_view()), name='joinhood'),
    path('admin/set/<str:hood_name>/<str:user_name>', login_required(UpdateHoodAdminView.as_view()), name='sethoodadmin'),
    path('profiles/', login_required(ProfileCreateView.as_view()), name='profiles'),
    path('profile/<str:user_name>', login_required(ProfileDetailsView.as_view()), name='specificprofile'),
    path('posts/', login_required(PostListCreateView.as_view()), name='posts'),
    path('bussinesses/', login_required(BussinessListCreateView.as_view()), name='bussinesses'),
    path('services/', login_required(EmergencyServiceListCreateView.as_view()), name='emergencyservice'),
]
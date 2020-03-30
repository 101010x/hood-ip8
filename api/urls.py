from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('hoods/', HoodCreateView.as_view(), name='hoods'),
    path('hood/<int:id>/', HoodDetailsView.as_view(), name='specifichood'),
    path('join/<int:hood_id>/<int:user_id>', UpdateHoodOptionJoinView.as_view(), name='joinhood'),
    path('admin/set/<int:hood_id>/<str:search_name>', UpdateHoodAdminView.as_view(), name='sethoodadmin'),
    path('profiles/', ProfileCreateView.as_view(), name='profiles'),
    path('profile/<int:id>', ProfileDetailsView.as_view(), name='specificprofile'),
    path('posts/', PostListCreateView.as_view(), name='posts'),
    path('bussinesses/', BussinessListCreateView.as_view(), name='bussinesses'),
    path('services/', EmergencyServiceListCreateView.as_view(), name='emergencyservice'),
]
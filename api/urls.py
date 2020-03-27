from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('hoods/', HoodCreateView.as_view(), name='hoods'),
    path('hood/<int:id>/', HoodDetailsView.as_view(), name='specifichood'),
    path('profiles/', ProfileCreateView.as_view(), name='profiles'),
    path('profile/<int:id>', ProfileDetailsView.as_view(), name='specificprofile'),
    
]
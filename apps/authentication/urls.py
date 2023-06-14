from django.urls import path
from . import views
from apps.authentication.services.auth_token import CustomTokenObtainPairView

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(),name="login-v1"),
    path("register/", views.RegisterUser.as_view(), name="register-v1"),
    path('user/', views.DetailsUser.as_view(), name='user')
]

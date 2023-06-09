from django.urls import path
from . import views
from apps.authentication.services.auth_token import CustomTokenObtainPairView

urlpatterns = [
    path("login/v1", CustomTokenObtainPairView.as_view(),name="login-v1"),
    path("register/v1", views.RegisterUser.as_view(), name="register-v1")
]

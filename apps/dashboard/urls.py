from django.urls import path
from . import views

urlpatterns = [
    path("", views.DashboardInfo.as_view(),name="my-stock-v1")
]

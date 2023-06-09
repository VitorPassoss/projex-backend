from django.urls import path
from . import views

urlpatterns = [
    path("v1", views.GetMyProperties.as_view(),name="my-stock-v1"),
    path("history/v1", views.GetMyHistory.as_view(),name="my-stock-v1"),
    path("create/v1", views.CreateProperties.as_view(),name="create-properties-v1"),
]

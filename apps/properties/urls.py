from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetMyProperties.as_view(),name="my-stock-v1"),
    path("history/", views.GetMyHistory.as_view(),name="my-stock-v1"),
    path("create/", views.CreateProperties.as_view(),name="create-properties-v1"),
]

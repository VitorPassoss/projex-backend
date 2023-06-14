from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/auth/', include('apps.authentication.urls')),
    path('v1/property/', include('apps.properties.urls')),
    path('v1/dashboard/', include('apps.dashboard.urls')),
    path('admin/', admin.site.urls),
]

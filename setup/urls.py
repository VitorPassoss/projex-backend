from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('property/', include('apps.properties.urls')),
    path('admin/', admin.site.urls),
]

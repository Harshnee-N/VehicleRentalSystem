from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rentals.urls')),          # Web UI
    path('api/', include('rentals.api_urls')),   # REST API
]

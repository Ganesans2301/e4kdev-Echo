from django.contrib import admin
from django.urls import path,include
from .admin import AppErrorAdmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/AppMessage/', include('AppMessage.urls')), 
    # Other URLs...
]

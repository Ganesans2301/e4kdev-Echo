# urls.py

from django.urls import path
from .views import serve_external_image,handle_file_upload

urlpatterns = [
    # Your other URL patterns
    path('images/<str:image_name>/', serve_external_image, name='serve_external_image'),
    path('upload/', handle_file_upload, name='handle_file_upload'),
]

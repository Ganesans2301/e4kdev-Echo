from django.shortcuts import render

# views.py

from django.http import FileResponse, Http404
import os
from django.conf import settings
from django.http import JsonResponse

def serve_external_image(request, image_name):
    file_path = os.path.join(settings.EXTERNAL_IMAGES_DIR, image_name)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='image/png')  # Adjust the content type based on your image format
    else:
        raise Http404("Image not found")
    

# views.py





def handle_file_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_path = os.path.join(settings.NEXTJS_PUBLIC_DIR, uploaded_file.name)
        
        try:
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        # Return the file path to the frontend
        relative_file_path = os.path.join('uploads', uploaded_file.name)
        return JsonResponse({'filePath': relative_file_path})
    else:
        return JsonResponse({'error': 'File not found or method not allowed'}, status=400)



# from django.contrib import admin
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import DummyModel
# from .utils import JsonDataFrame  # Ensure this import matches your project structure

# class AppErrorAdmin(admin.ModelAdmin):
#     change_list_template = "admin/app_error_change_list.html"
    
#     def get_urls(self):
#         from django.urls import path
#         urls = super().get_urls()
#         custom_urls = [
#             path('add/', self.admin_site.admin_view(self.add_view), name='app-error_add'),
#             path('update/<int:id>/', self.admin_site.admin_view(self.update_view), name='app-error_update'),
#             path('delete/<int:id>/', self.admin_site.admin_view(self.delete_view), name='app-error_delete'),
#         ]
#         return custom_urls + urls

#     def changelist_view(self, request, extra_context=None):
#         dataframe = JsonDataFrame()
#         context = {
#             **self.admin_site.each_context(request),
#             "errors": dataframe.get_all(),
#         }
#         return render(request, "admin/app_error_change_list.html", context)

#     def add_view(self, request):
#         if request.method == "POST":
#             apiname = request.POST["apiname"]
#             errormessage = request.POST["errormessage"]
#             successmessage = request.POST["successmessage"]
#             dataframe = JsonDataFrame()
#             dataframe.add_entry(apiname, errormessage, successmessage)
#             return redirect('admin:app-error_changelist')
#         return render(request, "admin/app_error_add.html")

#     def update_view(self, request, id):
#         dataframe = JsonDataFrame()
#         entry = next((item for item in dataframe.get_all() if item["id"] == id), None)
#         if request.method == "POST":
#             apiname = request.POST["apiname"]
#             errormessage = request.POST["errormessage"]
#             successmessage = request.POST["successmessage"]
#             dataframe.update_entry(id, apiname, errormessage, successmessage)
#             return redirect('admin:app-error_changelist')
#         return render(request, "admin/app_error_update.html", {"entry": entry})

#     def delete_view(self, request, id):
#         dataframe = JsonDataFrame()
#         dataframe.delete_entry(id)
#         return redirect('admin:app-error_changelist')

# # Register DummyModel with the custom admin class
# admin.site.register(DummyModel, AppErrorAdmin)













# #@@@@@@@@@@@@@@@@@@@ wORK
# from django.contrib import admin
# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from .utils import JsonDataFrame  # Make sure this is correctly defined
# from .models import DummyModel

# class AppErrorAdmin(admin.ModelAdmin):
#     change_list_template = "admin/app_error_change_list.html"
    
#     def get_urls(self):
#         from django.urls import path
#         urls = super().get_urls()
#         custom_urls = [
#             path('add/', self.admin_site.admin_view(self.add_view), name='app-error_add'),
#             path('update/<int:id>/', self.admin_site.admin_view(self.update_view), name='app-error_update'),
#             path('delete/<int:id>/', self.admin_site.admin_view(self.delete_view), name='app-error_delete'),
#         ]
#         return custom_urls + urls

#     def changelist_view(self, request, extra_context=None):
#         dataframe = JsonDataFrame()
#         context = {
#             **self.admin_site.each_context(request),
#             "errors": dataframe.get_all(),
#         }
#         return render(request, "admin/app_error_change_list.html", context)

#     def add_view(self, request):
#         if request.method == "POST":
#             apiname = request.POST.get("apiname")
#             errormessage = request.POST.get("errormessage")
#             successmessage = request.POST.get("successmessage")
#             dataframe = JsonDataFrame()
#             dataframe.add_entry(apiname, errormessage, successmessage)
#             return redirect('admin:app-error_changelist')  # Ensure this name matches your URL
#         return render(request, "admin/app_error_add.html")

#     def update_view(self, request, id):
#         dataframe = JsonDataFrame()
#         entry = get_object_or_404(dataframe.get_all(), id=id)
#         if request.method == "POST":
#             apiname = request.POST.get("apiname")
#             errormessage = request.POST.get("errormessage")
#             successmessage = request.POST.get("successmessage")
#             dataframe.update_entry(id, apiname, errormessage, successmessage)
#             return redirect('admin:app-error_changelist')  # Ensure this name matches your URL
#         return render(request, "admin/app_error_update.html", {"entry": entry})

#     def delete_view(self, request, id):
#         dataframe = JsonDataFrame()
#         dataframe.delete_entry(id)
#         return redirect('admin:app-error_changelist')  # Ensure this name matches your URL

# admin.site.register(DummyModel, AppErrorAdmin)

####################### 3 cODE 
from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from .utils import JsonDataFrame  # Ensure this path is correct
from django.http import HttpResponse
from .models import Message

class AppErrorAdmin(admin.ModelAdmin):
    change_list_template = "admin/app_error_change_list.html"
    
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('add/', self.admin_site.admin_view(self.add_view), name='app-error_add'),
            path('update/<int:id>/', self.admin_site.admin_view(self.update_view), name='app-error_update'),
            path('delete/<int:id>/', self.admin_site.admin_view(self.delete_view), name='app-error_delete'),
        ]
        return custom_urls + urls

    def changelist_view(self, request, extra_context=None):
        dataframe = JsonDataFrame()
        context = {
            **self.admin_site.each_context(request),
            "errors": dataframe.get_all(),
        }
        return render(request, "admin/app_error_change_list.html", context)

    def add_view(self, request):
        if request.method == "POST":
            apiname = request.POST.get("apiname")
            errormessage = request.POST.get("errormessage")
            successmessage = request.POST.get("successmessage")
            dataframe = JsonDataFrame()
            dataframe.add_entry(apiname, errormessage, successmessage)
            return redirect('/admin/AppMessage/message')  # Ensure this name matches your URL
        return render(request, "admin/app_error_add.html")

    def update_view(self, request, id):
        dataframe = JsonDataFrame()
        entry = dataframe.get_entry(id)
        if not entry:
            return HttpResponse("Entry not found", status=404)
        
        if request.method == "POST":
            apiname = request.POST.get("apiname")
            errormessage = request.POST.get("errormessage")
            successmessage = request.POST.get("successmessage")
            dataframe.update_entry(id, apiname, errormessage, successmessage)
            return redirect('/admin/AppMessage/message')  # Ensure this name matches your URL
        
        return render(request, "admin/app_error_update.html", {"entry": entry})

    def delete_view(self, request, id):
        dataframe = JsonDataFrame()
        dataframe.delete_entry(id)
        return redirect('/admin/AppMessage/message')  # Ensure this name matches your URL

admin.site.register(Message, AppErrorAdmin)

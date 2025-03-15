from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("todos.urls")),
    path("admin/", admin.site.urls),
    
    # external   
    path("__reload__/", include("django_browser_reload.urls")),
]
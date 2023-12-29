from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("crud/", include("crud.urls")),
    path('admin/', admin.site.urls),
]
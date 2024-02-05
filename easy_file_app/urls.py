from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'easy_file_app'
urlpatterns = [
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib import admin
from .models import FileRequest, File

admin.site.register(FileRequest)
admin.site.register(File)
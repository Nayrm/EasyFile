from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FileRequest(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_reason = models.CharField(max_length=50)
    request_status = models.CharField(max_length=15, default='pending', choices=(('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')))

    def __str__(self):
        return f"{self.user_id} - {self.datetime}"


class File(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=15)
    file_title = models.CharField(max_length=50, unique=True)
    file_description = models.TextField(max_length=500, blank=True)
    file = models.FileField(upload_to='files/')
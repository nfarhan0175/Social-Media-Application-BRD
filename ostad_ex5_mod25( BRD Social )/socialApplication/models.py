from django.db import models
import os
from django.contrib.auth.models import User

def upload_file_directory_by_name(instance, filename):
    return os.path.join('form/media', 'uploads', instance.title, filename)

# Create your models here.
class addPost(models.Model): 
    title = models.CharField(max_length=50)
    description = models.TextField()
    photos = models.ImageField(upload_to=upload_file_directory_by_name,default="None")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
    


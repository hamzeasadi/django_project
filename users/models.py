from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """profile table"""
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    # upload_to='profile_pics' is a directory that images get upload to when we upload an image
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

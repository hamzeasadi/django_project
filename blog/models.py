from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """simple post class"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # if the user deleted this post will be deleted as well



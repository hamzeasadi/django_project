from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.home, name='blog-home'),
    path('about/', blog_views.about, name='blog-about'),
]
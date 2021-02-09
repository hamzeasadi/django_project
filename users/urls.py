from . import views as user_views
from django.urls import path

urlpatterns = [
    path('registration', user_views.registration, name='registration')
]

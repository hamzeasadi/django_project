from . import views as user_views
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('registration', user_views.registration, name='registration'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/update/', user_views.profile_update, name='profile-update')
]

# By default django looks for login/logout template at registration/login.html(logout.html)
# we can create a registration directory inside our template subdirectory in our users app but we can also
# tell django where should look for template: template_name='users/login.html'

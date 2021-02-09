from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from . import forms as F


def registration(request):
    if request.method == 'POST':
        form = F.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            myMessage = f'your account has been created! You are now able to log in'
            messages.success(request, myMessage)
            return redirect(to='login')

    else:
        form = F.UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')



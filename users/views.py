from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from . import forms as F
from django.contrib.auth.decorators import login_required



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


@login_required
def profile(request):
    return render(request, 'users/profile.html')

def profile_update(request):
    if request.method == 'POST':
        form = F.UserUpdateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            myMessage = f'{username} profile was updated!'
            messages.success(request, myMessage)
            return redirect(to='profile')
    else:
        form = F.UserUpdateForm()

    return render(request, 'users/profile_update.html', {'form': form})




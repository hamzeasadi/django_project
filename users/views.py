from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            myMessage = f'account created for {username}'
            messages.success(request, myMessage)
            return redirect(to='blog-home')

    else:
        form = UserCreationForm()

    return render(request, 'users/registration.html', {'form': form})

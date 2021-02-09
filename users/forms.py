from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    # Meta gives us a nested namespace for configurations and keeps the configurations in one place
    class Meta:
        model = User # this form interact with this model so when we say form.save() it
        # will save form field to the user
        fields = ['username', 'email', 'password1', 'password2'] # the fields that we wanna have on our form and
        # it should match with fields of the model


class UserUpdateForm(ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email']

class ProfileUpdateForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
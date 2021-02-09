from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    # Meta gives us a nested namespace for configurations and keeps the configurations in one place
    class Meta:
        model = User # this form interact with this model so when we say form.save() it
        # will save form field to the user
        fields = ['username', 'email', 'password1', 'password2'] # the fields that we wanna have on our form and
        # it should match with fields of the model
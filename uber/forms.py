from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RiderRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #is_Rider = models.BooleanField(default=False)
    class Meta:
        #the model we want this form to interacte with

        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class DriverRegisterForm(UserCreationForm):
    email = forms.EmailField()
    car = forms.CharField(required=True)
    capacity = forms.IntegerField(required=True)
    class Meta:
        #the model we want this form to interacte with

        model = User
        fields = ['username', 'email', 'password1', 'password2', 'car', 'capacity']
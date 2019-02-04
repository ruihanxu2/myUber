from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Rides
from datetime import datetime




class RiderRegisterForm(UserCreationForm):
    email = forms.EmailField()


    #is_Rider = models.BooleanField(default=False)
    class Meta:
        #the model we want this form to interacte with

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DriverRegisterForm(UserCreationForm):
    email = forms.EmailField()
    vehicle_type = forms.CharField(required=True)
    plate_number = forms.IntegerField(required=True)
    max_passengers = forms.IntegerField(required=True)
    class Meta:
        #the model we want this form to interacte with

        model = User
        fields = ['username', 'email', 'password1', 'password2', 'vehicle_type','plate_number' ,'max_passengers']

class OpenNewRideForm(forms.ModelForm):

    destination = forms.CharField(required=True)
    expected_arrival = forms.DateTimeField(initial=datetime.now(), required=True)
    passenger_number = forms.IntegerField(required=True)
    vehicle_type = forms.CharField(required=True)
    #isConfirmed = models.BooleanField(default=False)  # a driver accepts this request
    #isComplete = models.BooleanField(default=False)  # a route is finished
    #is_driver = models.BooleanField(default=False)
    can_Share = forms.BooleanField(required=False)
    special_request = forms.CharField(required=False)

    class Meta:
        #the model we want this form to interacte with

        model = Rides
        fields = ['destination', 'expected_arrival', 'passenger_number', 'vehicle_type','can_Share' ,'special_request']


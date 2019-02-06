from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Rides, Share_Config
from datetime import datetime,timedelta




class RiderRegisterForm(UserCreationForm):
    email = forms.EmailField()


    #is_Rider = models.BooleanField(default=False)
    class Meta:
        #the model we want this form to interacte with

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DriverRegisterForm(UserCreationForm):
    email = forms.EmailField()
    vehicle_type = forms.ChoiceField(choices=(("car", "car"), ("suv", "suv"), ("van", "van")))
    plate_number = forms.IntegerField(required=True)
    max_passengers = forms.IntegerField(required=True)
    class Meta:
        #the model we want this form to interacte with

        model = User
        fields = ['username', 'email', 'password1', 'password2', 'vehicle_type','plate_number' ,'max_passengers']

class OpenNewRideForm(forms.ModelForm):

    destination = forms.CharField(required=True)
    expected_arrival = forms.DateTimeField(initial=datetime.now()+timedelta(hours=1), required=True)
    passenger_number = forms.IntegerField(required=True)
    isShare = forms.BooleanField(required=False, initial=False, label='Do you want to share with others?')
    vehicle_type = forms.ChoiceField(choices=(("car", "car"),("suv", "suv"), ("van", "van"))
                                     )

    special_request = forms.CharField(required=False)

    class Meta:
        #the model we want this form to interacte with

        model = Rides
        fields = ['destination', 'expected_arrival', 'passenger_number', 'vehicle_type','isShare' ,'special_request']


class ShareForm(forms.ModelForm):

    passengers = forms.IntegerField(required=True)
    destination = forms.CharField(max_length=100, required=True)
    expected_arrival_start = forms.DateTimeField(required=True, initial=datetime.now())
    expected_arrival_end = forms.DateTimeField(required=True, initial=datetime.now()+timedelta(hours=2))



    class Meta:
        #the model we want this form to interacte with

        model = Share_Config
        fields = ['passengers', 'destination', 'expected_arrival_start', 'expected_arrival_end']
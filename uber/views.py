from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RiderRegisterForm, DriverRegisterForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def home(request):
    return render(request, 'uber/home.html')



def register_driver(request):
    if request.method == 'POST':
        form = DriverRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(username=username,
                                            password=password, email=email)
            user_profile = Profile(user=user)
            user_profile.is_driver = True
            user_profile.plate_number = form.cleaned_data.get('plate_number')
            user_profile.max_passengers = form.cleaned_data.get('max_passengers')
            user_profile.save()
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')

    else:
        form = DriverRegisterForm()
    return render(request, 'uber/register_driver.html', {'form':form})

def register_rider(request):
    if request.method == 'POST':
        form = RiderRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')

    else:
        form = RiderRegisterForm()
    return render(request, 'uber/register_rider.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'uber/profile.html')
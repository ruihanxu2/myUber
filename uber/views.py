from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RiderRegisterForm, DriverRegisterForm
# Create your views here.
def home(request):
    return render(request, 'uber/home.html')



def register_driver(request):
    if request.method == 'POST':
        form = DriverRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
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
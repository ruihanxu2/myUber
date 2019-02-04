from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RiderRegisterForm, DriverRegisterForm, OpenNewRideForm
from django.contrib.auth.models import User
from .models import Profile, Rides
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
            user_profile.vehicle_type = form.cleaned_data.get('vehicle_type')
            user_profile.max_passengers = form.cleaned_data.get('max_passengers')
            user_profile.save()
            messages.success(request, f'Your account has been created! You are now able to login as a driver!')
            return redirect('login')

    else:
        form = DriverRegisterForm()
    return render(request, 'uber/register_driver.html', {'form':form})

def register_rider(request):
    if request.method == 'POST':
        form = OpenNewRideForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(username=username,
                                            password=password, email=email)
            user_profile = Profile(user=user)
            user_profile.is_driver = False
            user_profile.save()
            messages.success(request, f'Your account has been created! You are now able to login as a Rider!')
            return redirect('login')

    else:
        form = RiderRegisterForm()
    return render(request, 'uber/register_rider.html', {'form':form})

def new_ride(request):
    if request.method == 'POST':
        form = OpenNewRideForm(request.POST)
        if form.is_valid():
            # save_it = form.save(commit=False)
            newride = Rides(destination=form.cleaned_data['destination'],
                            expected_arrival=form.cleaned_data['expected_arrival'],
                            passenger_number=form.cleaned_data['passenger_number'],
                            rider_name=request.user.username,
                            )
            newride.save()
            newride.users.add(request.user)
            messages.success(request, f'You have just requested a ride!')
            return redirect('profile')
    else:
        # requested_rides = Rides.objects.filter(user=request.user, isComplete=False)
        # if len(requested_rides) != 0:
        #     request.session['message'] = 'You have unfinished ride.'
        #     return redirect('/accounts/passenger')
        # else:
            form = OpenNewRideForm()
            return render(request, 'uber/new_ride.html', {'form': form})


def search(request):
    return render(request, 'uber/search.html')

def search_share(request):
    return render(request, 'uber/search_share.html')

def search_past(request):
    return render(request, 'uber/search_past.html')

def search_cur(request):
    return render(request, 'uber/search_cur.html')

@login_required
def profile(request):
    return render(request, 'uber/profile.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RiderRegisterForm, DriverRegisterForm, OpenNewRideForm, ShareForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Profile, Rides, Share_Config
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
        form = RiderRegisterForm(request.POST)
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

            newride = Rides(destination=form.cleaned_data['destination'],
                            expected_arrival=form.cleaned_data['expected_arrival'],
                            passenger_number=form.cleaned_data['passenger_number'],
                            isShare=form.cleaned_data['isShare'],
                            vehicle_type=form.cleaned_data['vehicle_type'],
                            special_request =form.cleaned_data['special_request']
                            )
            #instance = newride.save(commit=False)
            newride.save()
            newride.ride_owner = request.user
            newride.save()
            messages.success(request, f'You have just requested a ride!')
            return redirect('profile')
    else:
            form = OpenNewRideForm()
            return render(request, 'uber/new_ride.html', {'form': form})
def search(request):
    #search all rides..
    capacity = request.user.profile.max_passengers
    car_type = request.user.profile.vehicle_type
    open_rides = Rides.objects.filter(isConfirmed=False, passenger_number__lte=capacity, vehicle_type=car_type)
    if (len(open_rides) == 0):
        messages.success(request, f'No open rides!')
        return redirect('profile')

    else:

        return render(request, 'uber/search.html', {'open_rides':open_rides})
def driver_confirm(request, ride_id):

    confirmride = Rides.objects.filter(id=ride_id)[0]
    confirmride.isConfirmed = True
    confirmride.driver_name = request.user.username
    confirmride.save()
    messages.success(request, f'You have just confirmed a ride!')
    # requested_rides = Rides.objects.filter(user=request.user, isComplete=False)
    # if len(requested_rides) != 0:
    #     request.session['message'] = 'You have unfinished ride.'
    #     return redirect('/accounts/passenger')
    # else:
    return render(request, 'uber/driver_confirm.html')
def driver_complete(request, ride_id):
    completeride = Rides.objects.filter(id=ride_id)[0]
    completeride.isComplete  = True
    completeride.save()
    messages.success(request, f'Congrats! You finished a ride! You can view it in your past rides')
    return redirect('profile')
def edit_ride(request, ride_id):
    if request.method == 'POST':
        form = OpenNewRideForm(request.POST)
        if form.is_valid():
            editride = Rides.objects.filter(id=ride_id)[0]

            editride.destination=form.cleaned_data['destination']
            editride.expected_arrival =form.cleaned_data['expected_arrival']
            editride.passenger_number = form.cleaned_data['passenger_number']
            editride.isShare=form.cleaned_data['isShare']
            editride.vehicle_type = form.cleaned_data['vehicle_type']
            editride.special_request =form.cleaned_data['special_request']
            editride.save()
            messages.success(request, f'You have just edited a ride!')
            return redirect('profile')
    else:
            editride = Rides.objects.filter(id=ride_id)[0]
            form = OpenNewRideForm(instance=editride)
            return render(request, 'uber/edit_ride.html', {'form': form})

def share(request, ride_id):
    shared_ride = Rides.objects.filter(id=ride_id)[0]
    shared_ride.ride_sharer.add(request.user)
    shared_ride.save()
    messages.success(request, f'Congrats! You have shared a ride with other people!')
    return redirect('profile')


def search_share(request):
    no_pass=request.user.share_config.passengers
    des = request.user.share_config.destination
    start = request.user.share_config.expected_arrival_start
    end = request.user.share_config.expected_arrival_end
    Share_Config.objects.filter()[0].delete()
    shareride = Rides.objects.filter(~Q(ride_owner=request.user),
                                     ~Q(ride_sharer=request.user),
                                     isShare=True,
                                     destination=des,
                                     passenger_number = no_pass,
                                     expected_arrival__range=[start, end],
                                     isConfirmed=False )

    if (len(shareride) == 0):
        messages.success(request, f'Sorry. No rides are availiable to share')
        return redirect('profile')

    else:

        return render(request, 'uber/search_share.html', {'share_rides': shareride})



def share_config(request):
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            user = request.user

            shareconfig = Share_Config(user=user)
            shareconfig.passengers = form.cleaned_data.get('passengers')
            shareconfig.destination = form.cleaned_data.get('destination')
            shareconfig.expected_arrival_start = form.cleaned_data.get('expected_arrival_start')
            shareconfig.expected_arrival_end = form.cleaned_data.get('expected_arrival_end')
            shareconfig.save()
            return HttpResponseRedirect('../search_share')

    else:
        form = ShareForm()
        return render(request, 'uber/share_config.html', {'form':form})

def search_past(request):
    past_rides_user = Rides.objects.filter(ride_owner=request.user, isComplete=True)
    past_rides_driver = Rides.objects.filter(driver_name=request.user.username, isComplete=True)

    return render(request, 'uber/search_past.html', {'past_rides_user':past_rides_user, 'past_rides_driver':past_rides_driver})


def search_cur(request):
    owned_rides = Rides.objects.filter(ride_owner=request.user, isComplete=False)
    owned_rides_driver = Rides.objects.filter(driver_name=request.user.username, isComplete=False, isConfirmed = True)

    shared_rides =  Rides.objects.filter(ride_sharer=request.user, isComplete=False)
    if(request.user.profile.is_driver):
        if (len(owned_rides_driver) == 0):
            messages.success(request, f'You have no cur rides')
            return redirect('profile')

        else:

            return render(request, 'uber/search_cur.html', {'owned_rides_driver': owned_rides_driver})

    else:
        if (len(owned_rides) == 0 and len(shared_rides) == 0):
            messages.success(request, f'You have no cur rides')
            return redirect('profile')

        else:

            return render(request, 'uber/search_cur.html',{'owned_rides':owned_rides, 'shared_rides':shared_rides})

@login_required
def profile(request):
    return render(request, 'uber/profile.html')
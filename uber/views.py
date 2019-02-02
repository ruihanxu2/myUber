from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'uber/home.html')



def register_driver(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request, 'uber/register_driver.html', {'form':form})

def register_rider(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request, 'uber/register_rider.html', {'form':form})

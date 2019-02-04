from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    plate_number = models.CharField(max_length=8)
    vehicle_type = models.CharField(max_length=100, default='')
    max_passengers = models.IntegerField(default=4)
    def __str__(self):
        return f'{self.user.username} Profile'


class Rides(models.Model):
    #all user
    ride_owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #driver
    driver_name  = models.CharField(max_length=100, default='')
    #rider
    rider_name = models.CharField(max_length=100, default='')
    destination = models.CharField(max_length=100, default='')
    expected_arrival = models.DateTimeField(default=timezone.now)
    passenger_number = models.IntegerField(default='1')
    vehicle_type = models.CharField(max_length=100, default='')
    isConfirmed = models.BooleanField(default=False)  #a driver accepts this request
    isComplete = models.BooleanField(default=False)   #a route is finished
    can_Share = models.BooleanField(default=False)
    special_request = models.CharField(max_length=100, default='')
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# class Rider(models.Model):
#     rider_name = models.CharField(max_length=200)
#     rider_pwd = models.CharField(max_length=200)
#
#
# class Driver(models.Model):
#     driver_name = models.CharField(max_length=200)
#     plate_number = models.CharField(max_length=8)
#     max_passengers = models.IntegerField(validators = [
#         MinValueValidator(1)
#     ])
#
#
#     SEDAN = "SEDAN"
#     SUV = "SUV"
#     TRUCK = "TRUCK"
#     CAR_TYPE_CHOICES = (
#         (SEDAN, "Sedan"),
#         (SUV,  "SUV"),
#         (TRUCK, "TRUCK")
#     )
#     car_type = models.CharField(max_length=10,
#                                  choices = CAR_TYPE_CHOICES,
#                                  default = SEDAN)
#
#     specialInfo = models.TextField()
#
#
#
#
#
# class OpenRequest(models.Model):
#     #the start and ending address of the request
#     start_addr = models.CharField(max_length=200)
#     dest_addr = models.CharField(max_length=200)
#     # the start time of the request
#     start_time = models.DateTimeField()
#
#     SEDAN = "SEDAN"
#     SUV = "SUV"
#     TRUCK = "TRUCK"
#     CAR_TYPE_CHOICES = (
#         (SEDAN, "Sedan"),
#         (SUV, "SUV"),
#         (TRUCK, "TRUCK")
#     )
#     car_type = models.CharField(max_length=10,
#                                 choices=CAR_TYPE_CHOICES,
#                                 default=SEDAN)
#
#     #total num of passagering
#     owner_num = models.IntegerField(validators = [
#         MinValueValidator(1)
#     ])
#
#     #share
#     share = models.BooleanField()
#     share_num = models.IntegerField(default = 0)
#
#     #many to one for owner
#     owner = models.ForeignKey(Rider, on_delete=models.CASCADE)
#     #many to many for sharer
#     sharer = models.ManyToManyField(Rider)
#
#
# class ConfirmedRequest(models.Model):
#     #the start and ending address of the request
#     start_addr = models.CharField(max_length=200)
#     dest_addr = models.CharField(max_length=200)
#     # the start time of the request
#     start_time = models.DateTimeField()
#
#
#     #owner+sharer
#     owners = models.ForeignKey(Rider, on_delete=models.CASCADE)
#     shares = models.ManyToManyField(Rider)
#
#     driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
#
# class CompletedRequest(models.Model):
#     # the start and ending address of the request
#     start_addr = models.CharField(max_length=200)
#     dest_addr = models.CharField(max_length=200)
#     # the start and ending time of the request
#     start_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#
#
#     # owner+sharer
#     owners = models.ForeignKey(Rider, on_delete=models.CASCADE)
#     shares = models.ManyToManyField(Rider)
#
#     driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

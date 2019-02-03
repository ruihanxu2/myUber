from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=True)
    plate_number = models.CharField(max_length=8)
    max_passengers = models.IntegerField(default=4)
    def __str__(self):
        return f'{self.user.username} Profile'


# class Rides(models.Model):
#     #tobefill..
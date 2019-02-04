# Generated by Django 2.1.5 on 2019-02-04 05:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uber', '0005_auto_20190204_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rides',
            name='is_driver',
        ),
        migrations.RemoveField(
            model_name='rides',
            name='pick_vehicle_plate',
        ),
        migrations.RemoveField(
            model_name='rides',
            name='user',
        ),
        migrations.AddField(
            model_name='rides',
            name='driver_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='rides',
            name='rider_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='rides',
            name='special_request',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='rides',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
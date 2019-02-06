# Generated by Django 2.1.5 on 2019-02-06 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0005_rides_ride_sharer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='ride_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

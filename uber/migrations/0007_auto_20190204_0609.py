# Generated by Django 2.1.5 on 2019-02-04 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uber', '0006_auto_20190204_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rides',
            name='users',
        ),
        migrations.AddField(
            model_name='rides',
            name='ride_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
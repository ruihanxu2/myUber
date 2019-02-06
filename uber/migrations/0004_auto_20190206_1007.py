# Generated by Django 2.1.5 on 2019-02-06 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uber', '0003_auto_20190206_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passengers', models.IntegerField(default=1)),
                ('destination', models.CharField(default='', max_length=100)),
                ('expected_arrival_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('expected_arrival_end', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='rides',
            name='rider_name',
        ),
    ]
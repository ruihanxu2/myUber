"""assignment1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from uber import views as uber_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_driver/', uber_views.register_driver, name='register_driver'),
    path('register_rider/', uber_views.register_rider, name='register_rider'),
    path('login/', auth_views.LoginView.as_view(template_name='uber/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='uber/logout.html'), name='logout'),
    path('profile/', uber_views.profile, name='profile'),
    path('search/', uber_views.search, name='search'),
    path('new_ride/', uber_views.new_ride, name='new_ride'),
    path('search_share/', uber_views.search_share, name='search_share'),
    path('search_past/', uber_views.search_past, name='search_past'),
    path('search_cur/', uber_views.search_cur, name='search_cur'),
    path('edit_ride/<int:ride_id>/', uber_views.edit_ride, name='edit_ride'),
    path('driver_confirm/<int:ride_id>/', uber_views.driver_confirm, name='driver_confirm'),
    path('complete/<int:ride_id>/', uber_views.driver_complete, name='driver_complete'),
    path('share/<int:ride_id>/', uber_views.share, name='share'),
    path('share_config/', uber_views.share_config, name='share_config'),
    path('search_share/', uber_views.search_share, name='search_share'),


    path('',uber_views.home, name='home' )

]

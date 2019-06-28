from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import datetime as dt
from .models import Profile, Restaurant
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db import models
from django.http import Http404
from .forms import RestaurantForm,ProfileForm,PostForm
from django.http import JsonResponse
import requests

# Create your views here.
def index(request):
    title = 'Home'
    restaurant = Restaurant.objects.all()

    return render(request, 'index.html', {'title':title  ,'restaurant':restaurant })

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile} Instagram photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details})


def restaurant(request):
   url = 'https://sleepy-garden-51801.herokuapp.com/json/s/Chicken%20Inn'
   response = requests.get(url)

   menu = response.json()

   return render(request, 'restaurants.html',{
       'search' : menu['searchedByName'],

   })

@login_required(login_url='/accounts/login/')
def new_restaurant(request):
    current_user = request.user

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.user = current_user
            restaurant.profile = profile
            restaurant.save()
        return redirect('index')
    else:
        form = RestaurantForm()
    return render(request, 'new_restaurant.html', {"form": form})

def get_menu():
   '''
   Fetches and returns random quotes from api
   '''

   url = 'https://sleepy-garden-51801.herokuapp.com/json/allItems'
   response = requests.get(url)

   menu = response.json()

   return menu

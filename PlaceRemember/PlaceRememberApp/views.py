from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from decimal import Decimal

def index(request):
    return render(request, 'PlaceRememberApp\index.html', context={'title' : 'PlaceRemember'})

def home(request):
    user = User.objects.get(pk=request.user.pk)
    places = user.account.places
    photo = user.account.photo
    context = {
        'places' : places,
        'photo' : photo,
        'title': 'Home'
    }
    return render(request, 'PlaceRememberApp\home.html', context)

def placeView(request, id):
    if id == 'add':
        currentPlace = Place()
        currentPlace.comment = ''
        currentPlace.lat = 55.74
        currentPlace.lng = 37.63
        user = User.objects.get(pk=request.user.pk)
        currentPlace.account = user.account
    else:
        currentPlace = Place.objects.get(id = id)

    if request.method == "POST":
        currentPlace.name = request.POST.get("name")
        currentPlace.comment = request.POST.get("comment")
        currentPlace.lat = Decimal(str(request.POST.get("lat")).replace(',','.'))
        currentPlace.lng = Decimal(str(request.POST.get("lng")).replace(',','.'))
        currentPlace.save()
        return redirect('home')
    else:
        return render(request, "PlaceRememberApp\placeform.html", {"place": currentPlace, 'title': 'Ваше воспоминание'})
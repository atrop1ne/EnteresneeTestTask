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

def addPlace(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            user = User.objects.get(pk=request.user.pk)
            place.account = user.account
            place.save()
            return redirect('home')

    form = PlaceForm(request.POST)

    context = {
        'form': form,
        'title': 'Your memory'
    }

    return render(request, 'PlaceRememberApp\placeform.html', context)

def editPlace(request, id):
    try:
        currentPlace = Place.objects.get(id = id)

        if request.method == "POST":
            currentPlace.name = request.POST.get("name")
            currentPlace.comment = request.POST.get("comment")
            currentPlace.lat = Decimal(str(request.POST.get("lat")).replace(',','.'))
            currentPlace.lng = Decimal(str(request.POST.get("lng")).replace(',','.'))
            currentPlace.save()
            return redirect('home')
        else:
            return render(request, "PlaceRememberApp\edit.html", {"place": currentPlace, 'title': 'Изменить воспоминание'})
    except Place.DoesNotExist:
        return HttpResponseNotFound("<h2>Place not found</h2>")
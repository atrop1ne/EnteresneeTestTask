from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView

def index(request):
    return render(request, 'PlaceRememberApp\index.html')

def home(request):
    form = PlaceForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'PlaceRememberApp\home.html', context)
from django.shortcuts import render

def index(request):
    return render(request, 'PlaceRememberApp\index.html')

def home(request):
    return render(request, 'PlaceRememberApp\home.html')
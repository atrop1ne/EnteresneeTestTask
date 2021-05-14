from django.shortcuts import redirect, render
from .models import *
from .forms import *

def index(request):
    return render(request, 'PlaceRememberApp\index.html')

def home(request):
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
        'form': form
    }

    return render(request, 'PlaceRememberApp\home.html', context)
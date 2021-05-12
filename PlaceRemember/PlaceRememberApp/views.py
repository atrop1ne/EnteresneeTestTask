from django.shortcuts import render
from .models import *
from django.views.generic import CreateView

def index(request):
    return render(request, 'PlaceRememberApp\index.html')

class HomeView(CreateView):
    model = User
    template_name = 'PlaceRememberApp\home.html'
    fields = '__all__'

    def get_queryset(self):
        return User.objects.get(pk=self.request.user.pk)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home', views.home, name='home'),
    path('placeform/<id>', views.placeView, name='placeform'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.HomeView.as_view(), name='home')
]
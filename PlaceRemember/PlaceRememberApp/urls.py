from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home', views.home, name='home'),
    path('placeform', views.addPlace, name='placeform'),
    path('edit/<int:id>', views.editPlace, name='edit')
]
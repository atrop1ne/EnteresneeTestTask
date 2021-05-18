from django.test import TestCase
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import Client, RequestFactory
from .models import *
from django.contrib.auth import get_user_model
from .views import placeView
from django.urls import reverse

User = get_user_model()

class PlaceRememberTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username = 'testuser', password = 'password')
        self.place = Place.objects.create(
            name = 'placename',
            comment = 'comment',
            lat = 0.0,
            lng = 0.0,
            account = self.user.account
        )
        self.factory = RequestFactory()

    def test_placeExistInAccountPlaces(self):
        self.assertIn(self.place, self.user.account.places.all())

    def test_addPlaceWithPlaceView(self):
        context = {'place' : self.place}
        c = Client()
        c.post('placeView', context)
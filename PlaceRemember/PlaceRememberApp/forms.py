from .models import Place
from django.forms import ModelForm, TextInput, Textarea


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ["name", "comment", "lat", "lng"]
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название места'}),
            "comment": Textarea(attrs={'class': 'form-control', 'placeholder': 'Добавьте описание'}),
            "lat": TextInput(attrs={'class': 'form-control'}),
            "lng": TextInput(attrs={'class': 'form-control'}),
        }
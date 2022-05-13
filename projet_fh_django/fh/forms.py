from django.forms import ModelForm
from . import models
from .models import Faction
from django import forms


class FactionForm(ModelForm):
    class Meta:
        model = models.Faction
        fields = ('Nom','faction_image')
        labels = {
            'Nom':'',
            'faction_image':'',
        }

class HeroForm(ModelForm):
    class Meta:
        model = models.Hero
        fields = ('hero_img', 'Nom', 'Type', 'Difficulte')
        labels = {
            'hero_img':'',
            'Nom':'',
            'Type':'',
            'Difficulte':'',
        }
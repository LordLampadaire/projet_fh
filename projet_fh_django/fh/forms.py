from django.forms import ModelForm
from . import models
from .models import Faction
from django import forms


class FactionForm(ModelForm):
    class Meta:
        model = models.Faction
        fields = ('Nom',)
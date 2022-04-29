from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class FactionForm(ModelForm):
    class Meta:
        model = models.Faction
        fields = ('Nom',)
        labels = {
            'nom' : _('Nom de la faction'),
        }
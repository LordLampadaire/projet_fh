from django.shortcuts import render
from django.shortcuts import render
from .forms import FactionForm
from . import models
# Create your views here.
def index(request):
    return render(request, 'fh/index.html')

def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = FactionForm(request.POST)
        if form.is_valid(): # validation du formulaire.
            faction = form.save() # sauvegarde dans la base
            return render(request,"fh/index.html",{"faction" : faction}) # envoie vers une page d'affichage de la faction créé
        else:
            return render(request,"fh/ajout.html",{"form": form})
    else:
        form = FactionForm() # création d'un formulaire vide
        return render(request,"fh/ajout.html",{"form" : form})



def read(request, id):
    faction = models.Faction.objects.get(pk=id)
    return render(request,"fh/details.html",{"faction": faction})

def show(request):
  faction = list(models.Faction.objects.all())
  return render(request, 'index.html', {'faction': faction})
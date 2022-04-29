from django.shortcuts import render
from django.shortcuts import render
from .forms import FactionForm
from . import models
# Create your views here.
def index(request):
    return render(request, 'fh/index.html')

def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = FactionForm(request)
        if form.is_valid(): # validation du formulaire.
            faction = form.save() # sauvegarde dans la base
            return render(request,"fh/index.html",{"nom" : faction}) # envoie vers une page d'affichage de la faction créé
        else:
            return render(request,"fh/ajout.html",{"form": form})
    else:
        form = FactionForm() # création d'un formulaire vide
        return render(request,"fh/ajout.html",{"form" : form})

def traitement(request):
    fform = FactionForm(request.POST)
    if fform.is_valid():
        faction = fform.save()
        return render(request,"fh/index.html",{"nom" : faction})
    else:
        return  render(request,"fh/ajoute.html",{"form": fform})

def read(request, id):
    faction = models.Faction.objects.get(pk=id)
    return render(request,"crud/details.html",{"nom": faction})

def show(request):
    return render(request,"fh/index.html",{"nom" : models.Faction.objects.all() })
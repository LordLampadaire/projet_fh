from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import FactionForm
from . import models
from django import forms


# Create your views here.

def index(request):
    faction = list(models.Faction.objects.all())
    return render(request, 'fh/index.html', {'faction': faction})


def ajout(request):
    if request.method == "POST":  # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = FactionForm(request.POST)
        if form.is_valid():  # validation du formulaire.
            faction = form.save()  # sauvegarde dans la base
            return HttpResponseRedirect("/")
        else:
            return render(request, "fh/ajout.html", {"form": form})
    else:
        form = FactionForm()  # création d'un formulaire vide
        return render(request, "fh/ajout.html", {"form": form})


def details(request, id):
    faction = models.Faction.objects.get(pk=id)
    return render(request, "fh/details.html", {"faction": faction})


def delete(request, id):
    faction = models.Faction.objects.get(pk=id)
    faction.delete()
    return HttpResponseRedirect("/")


def update(request, id):
    faction = models.Faction.objects.get(pk = id)
    form = FactionForm(faction.dico())
    return render(request, "fh/update.html",{"form":form, "id": id})

def updatetraitement(request, id):

    fform = FactionForm(request.POST)
    if fform.is_valid():
        faction = fform.save(commit = False)
        faction.id = id
        faction.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "fh/update.html", {"form": fform, "id" : id})
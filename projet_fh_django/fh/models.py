from django.db import models
from django import forms

# Create your models here.
TYPE =[
    ('gardien','Gardien'),
    ('tank','Tank'),
    ('assassin','Assassin'),
    ('hybride','Hybride'),
]
DIFF =[
    ('facile','Facile'),
    ('intermédiaire','Intermédiare'),
    ('difficile','Difficile'),
]

class Faction(models.Model):  # déclare la classe Livre héritant de la classe Model, classede base des modèles

    Nom = models.CharField(max_length=100)  # défini un champs de type texte de 100caractères maximum
    faction_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def dico(self):
        return {"Nom":self.Nom, "faction_image":self.faction_image}


class Hero(models.Model):
    hero_img = models.ImageField(null=True, blank=True, upload_to="images/")
    Nom = models.CharField(max_length=100)
    Type = models.CharField(max_length=10, choices=TYPE, default= 'facile')
    Difficulte = models.CharField(max_length=15, choices=DIFF, default='gardien')
    faction = models.ForeignKey("faction", on_delete=models.CASCADE, default=None)
    def dico(self):
        return {"hero_img":self.hero_img, "Nom":self.Nom, "Type":self.Type, "Difficulte":self.Difficulte, "Faction": self.faction}

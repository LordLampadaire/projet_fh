from django.db import models

# Create your models here.


class Faction(models.Model): #déclare la classe Livre héritant de la classe Model, classede base des modèles

    Nom = models.CharField(max_length=100) # défini un champs de type texte de 100caractères maximum



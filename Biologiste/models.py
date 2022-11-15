from django.db import models

# Create your models here.

class Biologiste(models.Model):
    nom= models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    motdepasse = models.CharField(max_length=16)
    genre = models.CharField(max_length=10)
    numTel = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    dateNaissance = models.DateField()
    #nomUnité=models.FOREYKEY(Unité,)

    def __str__(self):
        return f'{self.nom} {self.prenom}'
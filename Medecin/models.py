from django.db import models

# Create your models here.
class Medecin(models.Model):
    nom= models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    motdepasse = models.CharField(max_length=16)
    genre = models.CharField(max_length=10)
    numTel = models.CharField(max_length=100)
    adresse= models.CharField(max_length=100)
    dateNaissance = models.DateField()
    specialite = models.CharField(max_length=50)

    def __str__(self):
        return  "%s %s" % (self.nom, self.prenom)

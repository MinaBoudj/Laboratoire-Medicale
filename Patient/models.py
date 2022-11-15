from django.db import models

# Create your models here.
 

class Patient(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	genre = models.CharField(max_length=10)
	numTel = models.CharField(max_length=10)
	adresse = models.CharField(max_length=100)
	dateNaissance = models.DateField()
	groupeSanguin = models.CharField(max_length=5)
	date_ajout = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return  "%s %s" % (self.nom, self.prenom)
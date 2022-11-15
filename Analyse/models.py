from django.db import models
from Patient.models import Patient
from Medecin.models import Medecin

# Create your models here.
class Service(models.Model):
    nomService = models.CharField(max_length=200, null=True)
    responsable = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True)
    telService = models.CharField(max_length=100)

    def __str__(self):
        return self.nomService



class AnalyseBiochimie(models.Model):
    nom = models.CharField(max_length=200, null=True)
    def __str__(self):
                return self.nom

    

class AnalyseParasitologie(models.Model):
    nom = models.CharField(max_length=200, null=True)
    def __str__(self):
                return self.nom



class AnalyseHémobiologie(models.Model):
    nom = models.CharField(max_length=200, null=True)
    def __str__(self):
                return self.nom

    

class AnalyseMicrobiologie(models.Model):
    nom = models.CharField(max_length=200, null=True)
    def __str__(self):
                return self.nom
   



class DemandeAnalyse(models.Model):
        nomPatient = models.CharField(max_length=200)   
        prenomPatient = models.CharField(max_length=200) 
        idPatient = models.PositiveIntegerField()
        age = models.PositiveIntegerField()
        service = models.CharField(max_length=200) 

        Nommedecin_demandeur = models.CharField(max_length=200) 
        Prenommedecin_demandeur = models.CharField(max_length=200) 

        date_ajout_demande = models.DateTimeField(auto_now_add=True)
        nb_prelevement = models.PositiveIntegerField()

        nature_prelevement = models.CharField(max_length=200)
        type_tube = models.CharField(max_length=200)
        Biochimie = models.ManyToManyField(AnalyseBiochimie)
        Parasitologie = models.ManyToManyField(AnalyseParasitologie)
        Microbiologie = models.ManyToManyField(AnalyseMicrobiologie)
        Hémobiologie = models.ManyToManyField(AnalyseHémobiologie)

        def __str__(self):
                return self.service

        


class Demande(models.Model):
        nomPatient = models.CharField(max_length=200)   
        prenomPatient = models.CharField(max_length=200) 
        idPatient = models.PositiveIntegerField()
        age = models.PositiveIntegerField()
        service = models.CharField(max_length=200) 

        Nommedecin_demandeur = models.CharField(max_length=200) 
        Prenommedecin_demandeur = models.CharField(max_length=200) 

        date_ajout_demande = models.DateTimeField(auto_now_add=True)
        nb_prelevement = models.PositiveIntegerField()
        
        Biochimie = models.ManyToManyField(AnalyseBiochimie)
        Parasitologie = models.ManyToManyField(AnalyseParasitologie)
        Microbiologie = models.ManyToManyField(AnalyseMicrobiologie)
        Hémobiologie = models.ManyToManyField(AnalyseHémobiologie)

        def __str__(self):
                return self.service

        
class Prelevement(models.Model):
    id_demande = models.PositiveIntegerField()
    nature_prelevement = models.CharField(max_length=200)
    type_tube = models.CharField(max_length=200)

    def __str__(self):
                return self.id_demande
from django import forms
from django.forms import widgets
from .models import *

NATURE_PRELEVEMENT=(('Sang','Sang'),
            ('Urine','Urine'),
            ('LCR','LCR'),
            ('Aisselle','Aisselle'),
            ('Pus','Pus'),)

TYPE_TUBE=(('Sec','Sec'),
               ('EDTA','EDTA'),
               ('Citrate','Citrate'),
               ('Hiparine','Hiparine'),)  
SERVICE=(('Externe','Externe'),
            ('POA','POA'),
            ('POB','POB'),
            ('COA','COA'),)

    
class ServiceForm(forms.Form):
    nomService =forms.CharField(max_length=100) 


class BiocimieForm(forms.Form):
    nom = forms.CharField(max_length=100)

class ParasitologieForm(forms.Form):
    nom = forms.CharField(max_length=100)
    
class MicroBiologieForm(forms.Form):
    nom = forms.CharField(max_length=100)

class EmobiologieForm(forms.Form):
    nom = forms.CharField(max_length=100)
 

           
class DemandeForm(forms.ModelForm):   
    class Meta:
        
        model = Demande
        fields = [ 'nomPatient' ,'prenomPatient' ,'idPatient','age' ,'service','Nommedecin_demandeur','Prenommedecin_demandeur','nb_prelevement','Biochimie','Parasitologie','Microbiologie','Hémobiologie']
        labels = {'nomPatient':'Nom Patient' ,'prenomPatient':'Prenom Patient','idPatient':'idPatient','age' :'Age','service':'Service','Nommedecin_demandeur' :'Nom Medecin demandeur','Prenommedecin_demandeur':'Prenom Medecin demandeur' ,'nb_prelevement':'nb_prelevement','Biochimie':'Biochimie','Parasitologie':'Parasitologie','Microbiologie':'Microbiologie','Hémobiologie':'Hémobiologie'}
        widgets = {
           'nomPatient' : forms.TextInput(attrs={'class': 'form-control'}),
           'prenomPatient' : forms.TextInput(attrs={'class': 'form-control'}),  
           'age' : forms.TextInput(attrs={'class':'form-control'}),                  
           'Nommedecin_demandeur':forms.TextInput(attrs={'class': 'form-control'}),
           'Prenommedecin_demandeur':forms.TextInput(attrs={'class': 'form-control'}), 
          # 'nb_prelevement': forms.TextInput(attrs={'class':'form-control'}),        
           'service':forms.Select(choices=SERVICE),
        }
        nb_prelevement = forms.IntegerField(max_value=5),
        idPatient = forms.IntegerField(max_value=200),
        Biochimie= forms.ModelMultipleChoiceField(queryset=AnalyseBiochimie.objects.all()),
        Parasitologie= forms.ModelMultipleChoiceField(queryset=AnalyseParasitologie.objects.all()),
        Microbiologie= forms.ModelMultipleChoiceField(queryset=AnalyseMicrobiologie.objects.all()),
        Hémobiologie= forms.ModelMultipleChoiceField(queryset=AnalyseHémobiologie.objects.all()),













#class DemandeAnalyseForm(forms.ModelForm):
 #   class Meta:
  #      model = DemandeAnalyse
   #     fields = [ 'Patient' ,'service' ,'medecin_demandeur','nbr_demande','nature_prelevement','nature_analyse','type_tube','Vomissement','Constipatient','fievre','examen_complet']
    #    labels = {'Patient':'Patient' ,'service':'service' ,'medecin_demandeur':'medecin_demandeur','nbr_demande':'nbr_demande','nature_prelevement':'nature_prelevement','nature_analyse':'nature_analyse','type_tube':'type_tube','Vomissement':'Vomissement','Constipatient':'Constipatient','fievre':'fievre','examen_complet':'examen_complet'}


     #   widgets = {
      #      'Patient': forms.TextInput(attrs={'class': 'form-control'}),
       #     'service': forms.TextInput(attrs={'class': 'form-control'}),
        #    'medecin_demandeur': forms.TextInput(attrs={'class': 'form-control'}),
         #   'nbr_demande': forms.TextInput(attrs={'class': 'form-control'}),
         #   'nature_prelevement': forms.Select(choices=NATURE_PRELEVEMENT),
          #  'nature_analyse': forms.Select(choices=NATURE_ANALYSE),
           # 'type_tube': forms.Select(choices=TYPE_TUBE),
            #'Vomissement':forms.Select(choices=REPONSE),
            #'Constipatient':forms.Select(choices=REPONSE),
          #  'fievre':forms.Select(choices=REPONSE),
           # 'examen_complet':forms.Select(choices=REPONSE),
            
        #}
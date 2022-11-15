from django import forms
from django.db.models.fields import CharField
from .models import Patient

SEXE = [
    ('Femme', 'Femme'),
    ('Homme', 'Homme'),
]

GROUPE =[
	('O+','O+'),
	('O-','O-'),
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
]

class PatientForm(forms.ModelForm):
    class Meta:
       model = Patient
       fields = ['nom','prenom','email','genre','numTel','adresse','dateNaissance','groupeSanguin']
       labels ={'nom':'nom','email':'email','genre':'genre','numTel':'numTel','adresse':'adresse','dateNaissance':'dateNaissance','groupeSanguin':'groupeSanguin'}
       widgets = {
            'nom':forms.TextInput(attrs={'class':'form-control'}),
            'prenom':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'genre':forms.Select(choices=SEXE),
            'numTel':forms.TextInput(attrs={'class':'form-control'}),
            'adresse':forms.TextInput(attrs={'class':'form-control'}),
            'dateNaissance':forms.TextInput(attrs={'class':'form-control'}),
            'groupeSanguin':forms.Select(choices=GROUPE),

        } 


class PatientSearcForm(forms.Form):
     nom = CharField(max_length=200)
     prenom = CharField(max_length=100)

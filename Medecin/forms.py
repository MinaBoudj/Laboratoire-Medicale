from django import forms
from .models import Medecin
SEXE = [
    ('Femme', 'Femme'),
    ('Homme', 'Homme'),
]

SPECIALITE =[
    ('Gynecologist','Gynecologist'),
    ('Surgeon ','Surgeon '),
    ('Psychiatrist','Psychiatrist'),
    ('Cardiologist','Cardiologist'),
    ('Dermatologist','Dermatologist'),
    ('Endocrinologist','Endocrinologist'),
    ('Gastroenterologist','Gastroenterologist'),
    ('Nephrologist','Nephrologist'),
    ('Ophthalmologist','Ophthalmologist'),
    ('Anesthesiologist','Anesthesiologist'),

]



class MedecinForm(forms.ModelForm):
    class Meta:
        model =Medecin
        fields = [ 'nom' ,'prenom' ,'email','genre','numTel','dateNaissance','specialite','adresse']
        labels = {'nom':'nom' ,'prenom':'prenom' ,'email ':'email','genre':'genre','numTel':'numTel','dateNaissance':'dateNaissance','specialite':'specialite','adresse':'adresse'}


        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(choices=SEXE),
            'numTel': forms.TextInput(attrs={'class': 'form-control'}),
            'dateNaissance': forms.TextInput(attrs={'class': 'form-control'}),
            'specialite': forms.Select(choices=SPECIALITE),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
        }
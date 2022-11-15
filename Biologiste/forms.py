from django import forms
from .models import Biologiste
SEXE = [
    ('Femme', 'Femme'),
    ('Homme', 'Homme'),
]





class BiologisteForm(forms.ModelForm):
    class Meta:
        model =Biologiste
        fields = [ 'nom' ,'prenom' ,'email','genre','numTel','dateNaissance','adresse']
        labels = {'nom':'nom' ,'prenom':'prenom' ,'email ':'email','genre':'genre','numTel':'numTel','dateNaissance':'dateNaissance','adresse':'adresse'}


        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(choices=SEXE),
            'numTel': forms.TextInput(attrs={'class': 'form-control'}),
            'dateNaissance': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
        }
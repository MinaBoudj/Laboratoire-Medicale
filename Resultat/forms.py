from django import forms
from django.forms import widgets
from .models import *

GROUPE = [
    ('O', 'O'),
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
]

RH = [
    ('Positive', 'Positive'),
    ('Négative', 'Négative'),

]


class CoproForm(forms.ModelForm):
    class Meta:
        model = coproparasitologie
        fields = ['id_demande', 'Resultat', 'Macroscopie', 'Microscopie', 'Etat_frais', 'Ritchie', 'Kato_willis',
                  'Scotch_test', 'Autres']
        labels = {'id_demande': 'id Demande', 'Resultat': 'Resultat', 'Macroscopie': 'Macroscopie',
                  'Microscopie': 'Microscopie', 'Etat_frais': 'Etat_frais', 'Ritchie': 'Ritchie',
                  'Kato_willis': 'Kato_willis', 'Scotch_test': 'Scotch_test', 'Autres': 'Autres'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Resultat': forms.TextInput(attrs={'class': 'form-control'}),
            'Macroscopie': forms.TextInput(attrs={'class': 'form-control'}),
            'Microscopie': forms.TextInput(attrs={'class': 'form-control'}),
            'Etat_frais': forms.TextInput(attrs={'class': 'form-control'}),
            'Ritchie': forms.TextInput(attrs={'class': 'form-control'}),
            'Kato_willis': forms.TextInput(attrs={'class': 'form-control'}),
            'Scotch_test': forms.TextInput(attrs={'class': 'form-control'}),
            'Autres': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EntérocoqueForm(forms.ModelForm):
    class Meta:
        model = Entérocoque
        fields = ['id_demande', 'Ampi_amo', 'Getamicine', 'Strepto', 'Erythromicine', 'Furanes', 'Tetracy',
                  'Vancomicine', 'Tricoplanine', 'Ciprofloxacine',
                  'Rifampicine', 'Fosfomycine', 'Chloram', 'Tigecycline', 'Praticien']
        labels = {'id_demande': 'Id Demande', 'Ampi_amo': 'Ampi_amo', 'Getamicine': 'Getamicine', 'Strepto': 'Strepto',
                  'Erythromicine': 'Erythromicine',
                  'Furanes': 'Furanes', 'Tetracy': 'Tetracy', 'Vancomicine': 'Vancomicine',
                  'Tricoplanine': 'Tricoplanine', 'Ciprofloxacine': 'Ciprofloxacine',
                  'Rifampicine': 'Rifampicine', 'Fosfomycine': 'Fosfomycine', 'Chloram': 'Chloram',
                  'Tigecycline': 'Tigecycline', 'Praticien': 'Praticien'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Ampi_amo': forms.TextInput(attrs={'class': 'form-control'}),
            'Getamicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Strepto': forms.TextInput(attrs={'class': 'form-control'}),
            'Erythromicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Furanes': forms.TextInput(attrs={'class': 'form-control'}),
            'Tetracy': forms.TextInput(attrs={'class': 'form-control'}),
            'Vancomicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Tricoplanine': forms.TextInput(attrs={'class': 'form-control'}),
            'Ciprofloxacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Rifampicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Fosfomycine': forms.TextInput(attrs={'class': 'form-control'}),
            'Chloram': forms.TextInput(attrs={'class': 'form-control'}),
            'Tigecycline': forms.TextInput(attrs={'class': 'form-control'}),
            'Praticien': forms.TextInput(attrs={'class': 'form-control'}),

        }


class EntérobactériesForm(forms.ModelForm):
    class Meta:
        model = Entérobactéries
        fields = ['id_demande', 'Fosfomycine', 'Acide_nalid', 'Trime_sulfam', 'Ciprofloxacine', 'Furanes', 'Chloram',
                  'Colistine', 'Getamicine', 'Amikacine',
                  'Ertapéneme', 'Imipéneme', 'Céfrazidime', 'Aztréonam', 'Cefo_Ceftria', 'Cefoxitine', 'Amoxi_Acide',
                  'Ampi_amo', 'Praticien']
        labels = {'id_demande': 'Id Demande', 'Fosfomycine': 'Fosfomycine', 'Acide_nalid': 'Acide_nalid',
                  'Trime_sulfam': 'Trime_sulfam', 'Ciprofloxacine': 'Ciprofloxacine',
                  'Furanes': 'Furanes', 'Chloram': 'Chloram', 'Colistine': 'Colistine', 'Getamicine': 'Getamicine',
                  'Amikacine': 'Amikacine', 'Ertapéneme': 'Ertapéneme',
                  'Imipéneme': 'Imipéneme', 'Céfrazidime': 'Céfrazidime', 'Aztréonam': 'Aztréonam',
                  'Cefo_Ceftria': 'Cefo_Ceftria', 'Cefoxitine': 'Cefoxitine', 'Amoxi_Acide': 'Amoxi_Acide',
                  'Ampi_amo': 'Ampi_amo', 'Praticien': 'Praticien'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Fosfomycine': forms.TextInput(attrs={'class': 'form-control'}),
            'Acide_nalid': forms.TextInput(attrs={'class': 'form-control'}),
            'Trime_sulfam': forms.TextInput(attrs={'class': 'form-control'}),
            'Ciprofloxacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Furanes': forms.TextInput(attrs={'class': 'form-control'}),
            'Chloram': forms.TextInput(attrs={'class': 'form-control'}),
            'Colistine': forms.TextInput(attrs={'class': 'form-control'}),
            'Getamicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Amikacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Ertapéneme': forms.TextInput(attrs={'class': 'form-control'}),
            'Imipéneme': forms.TextInput(attrs={'class': 'form-control'}),
            'Céfrazidime': forms.TextInput(attrs={'class': 'form-control'}),
            'Aztréonam': forms.TextInput(attrs={'class': 'form-control'}),
            'Cefo_Ceftria': forms.TextInput(attrs={'class': 'form-control'}),
            'Cefoxitine': forms.TextInput(attrs={'class': 'form-control'}),
            'Cefazoline': forms.TextInput(attrs={'class': 'form-control'}),
            'Amoxi_Acide': forms.TextInput(attrs={'class': 'form-control'}),
            'Ampi_amo': forms.TextInput(attrs={'class': 'form-control'}),
            'Praticien': forms.TextInput(attrs={'class': 'form-control'}),

        }


class BactériologieForm(forms.ModelForm):
    class Meta:
        model = bactériologie
        fields = ['id_demande', 'Reference', 'Cytologie', 'Culture']
        labels = {'id_demande': 'Id Demande', 'Reference': 'Reference', 'Cytologie': 'Cytologie', 'Culture': 'Culture'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Reference': forms.TextInput(attrs={'class': 'form-control'}),
            'Cytologie': forms.TextInput(attrs={'class': 'form-control'}),
            'Culture': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FNSForm(forms.ModelForm):
    class Meta:
        model = FNS
        fields = ['id_demande', 'GB', 'GR', 'Hb', 'VGM', 'Hte', 'TCMH', 'CCMH', 'Ptte']
        labels = {'id_demande': 'Id Demande', 'GB': 'GB', 'GR': 'GR', 'Hb': 'Hb', 'VGM': 'VGM', 'Hte': 'Hte',
                  'TCMH': 'TCMH', 'CCMH': 'CCMH', 'Ptte': 'Ptte'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'GB': forms.TextInput(attrs={'class': 'form-control'}),
            'GR': forms.TextInput(attrs={'class': 'form-control'}),
            'Hb': forms.TextInput(attrs={'class': 'form-control'}),
            'VGM': forms.TextInput(attrs={'class': 'form-control'}),
            'Hte': forms.TextInput(attrs={'class': 'form-control'}),
            'TCMH': forms.TextInput(attrs={'class': 'form-control'}),
            'CCMH': forms.TextInput(attrs={'class': 'form-control'}),
            'Ptte': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PseudoForm(forms.ModelForm):
    class Meta:
        model = Pseudomonas
        fields = ['id_demande', 'Titracine', 'Piperacilline', 'Ticar_Acide', 'Ceftazidime', 'Aztreonam', 'Imipéneme',
                  'Amikacine', 'Gentamicine', 'Cipro', 'Lévofloxacine', 'Fosfomycine', 'Colistine', 'Praticien']
        labels = {'id_demande': 'Id Demande', 'Titracine': 'Titracine', 'Piperacilline': 'Piperacilline',
                  'Ticar_Acide': 'Ticar_Acide', 'Ceftazidime': 'Ceftazidime', 'Aztreonam': 'Aztreonam',
                  'Imipéneme': 'Imipéneme', 'Amikacine': 'Amikacine', 'Gentamicine': 'Gentamicine', 'Cipro': 'Cipro',
                  'Lévofloxacine': 'Lévofloxacine', 'Fosfomycine': 'Fosfomycine', 'Colistine': 'Colistine',
                  'Praticien': 'Praticien'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Titracine': forms.TextInput(attrs={'class': 'form-control'}),
            'Piperacilline': forms.TextInput(attrs={'class': 'form-control'}),
            'Ticar_Acide': forms.TextInput(attrs={'class': 'form-control'}),
            'Ceftazidime': forms.TextInput(attrs={'class': 'form-control'}),
            'Aztreonam': forms.TextInput(attrs={'class': 'form-control'}),
            'Imipéneme': forms.TextInput(attrs={'class': 'form-control'}),
            'Amikacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Gentamicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Cipro': forms.TextInput(attrs={'class': 'form-control'}),
            'Lévofloxacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Fosfomycine': forms.TextInput(attrs={'class': 'form-control'}),
            'Colistine': forms.TextInput(attrs={'class': 'form-control'}),
            'Praticien': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AcinetoForm(forms.ModelForm):
    class Meta:
        model = Acinetobacter
        fields = ['id_demande', 'Ticarcilline', 'Piperacilline', 'Ticar_Acide', 'Ceftazidime', 'Imipéneme', 'Amikacine',
                  'Gentamicine', 'Tobramycine', 'Netilmicine', 'Ciprof', 'Lévofloxamine', 'Tetracy_doxy',
                  'Trime_sulfam', 'Colistine', 'Praticie']
        labels = {'id_demande': 'Id Demande', 'Ticarcilline': 'Ticarcilline', 'Piperacilline': 'Piperacilline',
                  'Ticar_Acide': 'Ticar_Acide', 'Ceftazidime': 'Ceftazidime', 'Imipéneme': 'Imipéneme',
                  'Amikacine': 'Amikacine', 'Gentamicine': 'Gentamicine', 'Tobramycine': 'Tobramycine',
                  'Netilmicine': 'Netilmicine', 'Ciprof': 'Ciprof', 'Lévofloxamine': 'Lévofloxamine',
                  'Tetracy_doxy': 'Tetracy_doxy',
                  'Trime_sulfam': 'Trime_sulfam', 'Colistine': 'Colistine', 'Praticie': 'Praticie'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Ticarcilline': forms.TextInput(attrs={'class': 'form-control'}),
            'Piperacilline': forms.TextInput(attrs={'class': 'form-control'}),
            'Ticar_Acide': forms.TextInput(attrs={'class': 'form-control'}),
            'Ceftazidime': forms.TextInput(attrs={'class': 'form-control'}),
            'Imipéneme': forms.TextInput(attrs={'class': 'form-control'}),
            'Amikacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Gentamicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Tobramycine': forms.TextInput(attrs={'class': 'form-control'}),
            'Netilmicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Ciprof': forms.TextInput(attrs={'class': 'form-control'}),
            'Lévofloxamine': forms.TextInput(attrs={'class': 'form-control'}),
            'Tetracy_doxy': forms.TextInput(attrs={'class': 'form-control'}),
            'Trime_sulfam': forms.TextInput(attrs={'class': 'form-control'}),
            'Colistine': forms.TextInput(attrs={'class': 'form-control'}),
            'Praticie': forms.TextInput(attrs={'class': 'form-control'}),
        }


class GroupeForm(forms.ModelForm):
    class Meta:
        model = groupageSanguin
        fields = ['id_demande', 'Groupe', 'Rh']
        labels = {'id_demande': 'Id Demande', 'Groupe': 'Groupe', 'Rh': 'Rh'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Groupe': forms.Select(choices=GROUPE),
            'Rh': forms.Select(choices=RH),
        }


class BiocForm(forms.ModelForm):
    class Meta:
        model = BiochimieGénérale
        fields = ['id_demande', 'Glucose', 'Urée', 'Créatinine', 'Acide_Urique', 'Sodium', 'Potassium', 'Clicium_total',
                  'Calcium_ionisé', 'Phosphore', 'Magnésium', 'Fer',
                  'aspect_résum', 'Cholestérol_total', 'Triglycérides', 'HDL', 'LDL', 'Protéines', 'Albumine',
                  'Amylase', 'Lipase', 'CK_total', 'CK_Mb', 'LDH',
                  'GOT', 'GPT', 'PAL', 'y_gt', 'Bilirubine', 'Praticien']
        labels = {'id_demande': 'Id Demande', 'Glucose': 'Glucose', 'Urée': 'Urée', 'Créatinine': 'Créatinine',
                  'Acide_Urique': 'Acide_Urique', 'Sodium': 'Sodium', 'Potassium': 'Potassium',
                  'Clicium_total': 'Clicium_total', 'Calcium_ionisé': 'Calcium_ionisé', 'Phosphore': 'Phosphore',
                  'Magnésium': 'Magnésium', 'Fer': 'Fer',
                  'aspect_résum': 'aspect_résum', 'Cholestérol_total': 'Cholestérol_total',
                  'Triglycérides': 'Triglycérides', 'HDL': 'HDL', 'LDL': 'LDL', 'Protéines': 'Protéines',
                  'Albumine': 'Albumine', 'Amylase': 'Amylase', 'Lipase': 'Lipase', 'CK_total': 'CK_total',
                  'CK_Mb': 'CK_Mb', 'LDH': 'LDH',
                  'GOT': 'GOT', 'GPT': 'GPT', 'PAL': 'PAL', 'y_gt': 'y_gt', 'Bilirubine': 'Bilirubine',
                  'Praticien': 'Praticien'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Glucose': forms.TextInput(attrs={'class': 'form-control'}),
            'Urée': forms.TextInput(attrs={'class': 'form-control'}),
            'Créatinine': forms.TextInput(attrs={'class': 'form-control'}),
            'Acide_Urique': forms.TextInput(attrs={'class': 'form-control'}),
            'Sodium': forms.TextInput(attrs={'class': 'form-control'}),
            'Potassium': forms.TextInput(attrs={'class': 'form-control'}),
            'Clicium_total': forms.TextInput(attrs={'class': 'form-control'}),
            'Calcium_ionisé': forms.TextInput(attrs={'class': 'form-control'}),
            'Phosphore': forms.TextInput(attrs={'class': 'form-control'}),
            'Magnésium': forms.TextInput(attrs={'class': 'form-control'}),
            'Fer': forms.TextInput(attrs={'class': 'form-control'}),
            'aspect_résum': forms.TextInput(attrs={'class': 'form-control'}),
            'Cholestérol_total': forms.TextInput(attrs={'class': 'form-control'}),
            'Triglycérides': forms.TextInput(attrs={'class': 'form-control'}),
            'HDL': forms.TextInput(attrs={'class': 'form-control'}),
            'LDL': forms.TextInput(attrs={'class': 'form-control'}),
            'Protéines': forms.TextInput(attrs={'class': 'form-control'}),
            'Albumine': forms.TextInput(attrs={'class': 'form-control'}),
            'Amylase': forms.TextInput(attrs={'class': 'form-control'}),
            'Lipase': forms.TextInput(attrs={'class': 'form-control'}),
            'CK_total': forms.TextInput(attrs={'class': 'form-control'}),
            'CK_Mb': forms.TextInput(attrs={'class': 'form-control'}),
            'LDH': forms.TextInput(attrs={'class': 'form-control'}),
            'GOT': forms.TextInput(attrs={'class': 'form-control'}),
            'GPT': forms.TextInput(attrs={'class': 'form-control'}),
            'PAL': forms.TextInput(attrs={'class': 'form-control'}),
            'y_gt': forms.TextInput(attrs={'class': 'form-control'}),
            'Bilirubine': forms.TextInput(attrs={'class': 'form-control'}),
            'Praticien': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BilanForm(forms.ModelForm):
    class Meta:
        model = BilanDurgence
        fields = ['id_demande', 'Taux_pro', 'INR', 'Temp_cépha', 'Glucose', 'Urée', 'créatinine', 'Bilirubine',
                  'Calcium', 'CRP', 'WBC', 'RBC', 'HGB', 'HCT', 'MCV',
                  'MCH', 'MCHC', 'PLT', 'LYM', 'NEUT']
        labels = {'id_demande': 'Id Demande', 'Taux_pro': 'Taux_pro', 'INR': 'INR', 'Temp_cépha': 'Temp_cépha',
                  'Glucose': 'Glucose', 'Urée': 'Urée', 'créatinine': 'créatinine',
                  'Bilirubine': 'Bilirubine', 'Calcium': 'Calcium', 'CRP': 'CRP', 'WBC': 'WBC', 'RBC': 'RBC',
                  'HGB': 'HGB', 'HCT': 'HCT', 'MCV': 'MCV', 'MCH': 'MCH', 'MCHC': 'MCHC', 'PLT': 'PLT',
                  'LYM': 'LYM', 'NEUT': 'NEUT'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Taux_pro':forms.TextInput(attrs={'class': 'form-control'}),
            'INR': forms.TextInput(attrs={'class': 'form-control'}),
            'Temp_cépha': forms.TextInput(attrs={'class': 'form-control'}),
            'Glucose': forms.TextInput(attrs={'class': 'form-control'}),
            'Urée': forms.TextInput(attrs={'class': 'form-control'}),
            'créatinine': forms.TextInput(attrs={'class': 'form-control'}),
            'Bilirubine': forms.TextInput(attrs={'class': 'form-control'}),
            'Calcium': forms.TextInput(attrs={'class': 'form-control'}),
            'CRP': forms.TextInput(attrs={'class': 'form-control'}),
            'WBC':forms.TextInput(attrs={'class': 'form-control'}),
            'RBC': forms.TextInput(attrs={'class': 'form-control'}),
            'HGB': forms.TextInput(attrs={'class': 'form-control'}),
            'HCT': forms.TextInput(attrs={'class': 'form-control'}),
            'MCV': forms.TextInput(attrs={'class': 'form-control'}),
            'MCH': forms.TextInput(attrs={'class': 'form-control'}),
            'MCHC': forms.TextInput(attrs={'class': 'form-control'}),
            'PLT': forms.TextInput(attrs={'class': 'form-control'}),
            'LYM': forms.TextInput(attrs={'class': 'form-control'}),
            'NEUT': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StapyloForm(forms.ModelForm):
    class Meta:
        model = Stapylocoque
        fields = ['id_demande', 'Penicilline', 'Oxacilline', 'Cefoxitine', 'Amikacine', 'Gentamicine', 'Kanamycine',
                  'Eryth_Azith', 'Clind_linc', 'Prist_Quin_dal', 'Ofloxacine', 'Ciprofloxacine',
                  'Lévofloxacine', 'Chloram', 'Vancomycine', 'Rifampicine', 'Trime_sulfam', 'Tetracy_doxy',
                  'Acidefucidique']
        labels = {'id_demande': 'Id Demande', 'Penicilline': 'Penicilline', 'Oxacilline': 'Oxacilline',
                  'Cefoxitine': 'Cefoxitine', 'Amikacine': 'Amikacine', 'Gentamicine': 'Gentamicine',
                  'Kanamycine': 'Kanamycine', 'Eryth_Azith': 'Eryth_Azith', 'Clind_linc': 'Clind_linc',
                  'Prist_Quin_dal': 'Prist_Quin_dal', 'Ofloxacine': 'Ofloxacine', 'Ciprofloxacine': 'Ciprofloxacine',
                  'Lévofloxacine': 'Lévofloxacine', 'Chloram': 'Chloram', 'Vancomycine': 'Vancomycine',
                  'Rifampicine': 'Rifampicine', 'Trime_sulfam': 'Trime_sulfam', 'Tetracy_doxy': 'Tetracy_doxy',
                  'Acidefucidique': 'Acidefucidique'}
        widgets = {
            'id_demande': forms.TextInput(attrs={'class': 'form-control'}),
            'Penicilline': forms.TextInput(attrs={'class': 'form-control'}),
            'Oxacilline': forms.TextInput(attrs={'class': 'form-control'}),
            'Cefoxitine': forms.TextInput(attrs={'class': 'form-control'}),
            'Amikacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Gentamicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Kanamycine': forms.TextInput(attrs={'class': 'form-control'}),
            'Eryth_Azith': forms.TextInput(attrs={'class': 'form-control'}),
            'Clind_linc': forms.TextInput(attrs={'class': 'form-control'}),
            'Prist_Quin_dal': forms.TextInput(attrs={'class': 'form-control'}),
            'Ofloxacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Ciprofloxacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Lévofloxacine': forms.TextInput(attrs={'class': 'form-control'}),
            'Chloram': forms.TextInput(attrs={'class': 'form-control'}),
            'Vancomycine': forms.TextInput(attrs={'class': 'form-control'}),
            'Rifampicine': forms.TextInput(attrs={'class': 'form-control'}),
            'Trime_sulfam': forms.TextInput(attrs={'class': 'form-control'}),
            'Tetracy_doxy': forms.TextInput(attrs={'class': 'form-control'}),
            'Acidefucidique': forms.TextInput(attrs={'class': 'form-control'}),
        }

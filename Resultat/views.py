from typing import List

from django.views.decorators.csrf import csrf_exempt

from Analyse.forms import ParasitologieForm
from django.shortcuts import render, redirect

from Laboratoire import settings
from Patient.models import *
from Analyse.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# for generating pdf invoice
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os


# Create your views here.
def Resultats(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')

    return render(request, 'resultat/gestionResultat.html')


def ResultatUniteBiochimie(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')

    return render(request, 'resultat/Biochimie/ResultatUniteBiochimie.html')


def ResultatUniteParasitologie(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')

    return render(request, 'resultat/Parasitologie/ResultatUniteParasitologie.html')


def ResultatUnitéMicrobiologie(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')

    return render(request, 'resultat/Microbiologie/ResultatUnitéMicrobiologie.html')


def ResultatUniteHémobiologie(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')

    return render(request, 'resultat/Hémobiologie/ResultatUniteHémobiologie.html')


#################################       Unité Parasitologie          ##################################
def ajouterResultat_coproparasitologie(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        resultat = request.POST['Resultat']
        Macroscopie = request.POST['Macroscopie']
        Microscopie = request.POST['Microscopie']
        Etat_frais = request.POST['Etat_frais']
        Ritchie = request.POST['Ritchie']
        Kato_willis = request.POST['Kato_willis']
        Scotch_test = request.POST['Scotch_test']
        Autres = request.POST['Autres']

        try:

            coproparasitologie.objects.create(id_demande=pk, Resultat=resultat, Macroscopie=Macroscopie,
                                              Microscopie=Microscopie,
                                              Etat_frais=Etat_frais, Ritchie=Ritchie, Kato_willis=Kato_willis,
                                              Scotch_test=Scotch_test, Autres=Autres)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Parasitologie/ajouterCoproparasitologie.html', d)


def listeDemandeCopro(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Parasitologie.filter(nom__contains='coproparasitologie')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Parasitologie/coproparasitologie.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Parasitologie/coproparasitologie.html', e)


@login_required(login_url='PageAuthentification')
def voirCoproparasitologie(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    copro = coproparasitologie.objects.all()
    d = {'copro': copro}
    return render(request, 'resultat/Parasitologie/listeCopro.html', d)


def ajouterResultat_bacteriologie(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Reference = request.POST['Reference']
        Cytologie = request.POST['Cytologie']
        Culture = request.POST['Culture']

        try:
            bactériologie.objects.create(id_demande=pk, Reference=Reference, Cytologie=Cytologie, Culture=Culture)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Parasitologie/ajouterBactériologie.html', d)


def listeDemandeBactériologie(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Parasitologie.filter(nom__contains='bactériologie')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Parasitologie/bactériologie.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Parasitologie/bactériologie.html', e)


@login_required(login_url='PageAuthentification')
def voirBactériologie(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    bacterio = bactériologie.objects.all()
    d = {'bacterio': bacterio}
    return render(request, 'resultat/Parasitologie/listeBacterio.html', d)


def ajouterResultat_Entérocoque(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Ampi_amo = request.POST['Ampi_amo']
        Getamicine = request.POST['Getamicine']
        Strepto = request.POST['Strepto']
        Erythromicine = request.POST['Erythromicine']
        Furanes = request.POST['Furanes']
        Tetracy = request.POST['Tetracy']
        Vancomicine = request.POST['Vancomicine']
        Tricoplanine = request.POST['Tricoplanine']
        Ciprofloxacine = request.POST['Ciprofloxacine']
        Rifampicine = request.POST['Rifampicine']
        Fosfomycine = request.POST['Fosfomycine']
        Chloram = request.POST['Chloram']
        Tigecycline = request.POST['Tigecycline']
        Praticien = request.POST['Praticien']
        try:

            Entérocoque.objects.create(id_demande=pk, Ampi_amo=Ampi_amo, Getamicine=Getamicine, Strepto=Strepto,
                                       Erythromicine=Erythromicine,
                                       Furanes=Furanes, Tetracy=Tetracy, Vancomicine=Vancomicine,
                                       Tricoplanine=Tricoplanine, Ciprofloxacine=Ciprofloxacine,
                                       Rifampicine=Rifampicine,
                                       Fosfomycine=Fosfomycine, Chloram=Chloram, Tigecycline=Tigecycline,
                                       Praticien=Praticien)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Parasitologie/ajouterEntérocoque.html', d)


def listeDemandeEntérocoque(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Parasitologie.filter(nom__contains='Entérocoque')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Parasitologie/Entérocoque.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Parasitologie/Entérocoque.html', e)


@login_required(login_url='PageAuthentification')
def voirEntérocoque(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    enterobactéries = Entérocoque.objects.all()
    d = {'enterobactéries': enterobactéries}
    return render(request, 'resultat/Parasitologie/listeEntérocoque.html', d)


##############################   Unité Hémobiologie #############################

def ajouterResultat_GroupageSanguin(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Groupe = request.POST['Groupe']
        Rh = request.POST['Rh']
        try:

            groupageSanguin.objects.create(id_demande=pk, Groupe=Groupe, Rh=Rh)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Hémobiologie/ajouterGroupageSanguin.html', d)

    # for generating pdf invoice


@csrf_exempt
def listeDemandeGroupageSanguin(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Hémobiologie.filter(nom__contains='Groupage Sanguin')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Hémobiologie/GroupageSanguin.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Hémobiologie/GroupageSanguin.html', e)


@login_required(login_url='PageAuthentification')
def voirGroupageSanguin(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    groupage = groupageSanguin.objects.all()
    d = {'groupage': groupage}
    return render(request, 'resultat/Hémobiologie/listeGroupageSanguin.html', d)


def ajouterResultat_FNS(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        GB = request.POST['GB']
        GR = request.POST['GR']
        Hb = request.POST['Hb']
        VGM = request.POST['VGM']
        Hte = request.POST['Hte']
        TCMH = request.POST['TCMH']
        CCMH = request.POST['CCMH']
        Ptte = request.POST['Ptte']
        try:

            FNS.objects.create(id_demande=pk, GB=GB, GR=GR, Hb=Hb, VGM=VGM, Hte=Hte, TCMH=TCMH, CCMH=CCMH, Ptte=Ptte)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Hémobiologie/ajouterFNS.html', d)


def listeDemandeFNS(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Hémobiologie.filter(nom__contains='FNS')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Hémobiologie/FNS.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Hémobiologie/FNS.html', e)


@login_required(login_url='PageAuthentification')
def voirFNS(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    fns = FNS.objects.all()
    d = {'fns': fns}
    return render(request, 'resultat/Hémobiologie/listeFNS.html', d)


###########################   Unité Microbiologie   ###############################

def ajouterResultat_Pseudomonas(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Titracine = request.POST['Titracine']
        Piperacilline = request.POST['Piperacilline']
        Ticar_Acide = request.POST['Ticar_Acide']
        Ceftazidime = request.POST['Ceftazidime']
        Aztreonam = request.POST['Aztreonam']
        Imipéneme = request.POST['Imipéneme']
        Amikacine = request.POST['Amikacine']
        Gentamicine = request.POST['Gentamicine']
        Cipro = request.POST['Cipro']
        Lévofloxacine = request.POST['Lévofloxacine']
        Fosfomycine = request.POST['Fosfomycine']
        Colistine = request.POST['Colistine']
        Praticien = request.POST['Praticien']
        try:

            Pseudomonas.objects.create(id_demande=pk, Titracine=Titracine, Piperacilline=Piperacilline,
                                       Ticar_Acide=Ticar_Acide,
                                       Ceftazidime=Ceftazidime, Aztreonam=Aztreonam, Imipéneme=Imipéneme,
                                       Amikacine=Amikacine, Gentamicine=Gentamicine, Cipro=Cipro,
                                       Lévofloxacine=Lévofloxacine, Fosfomycine=Fosfomycine, Colistine=Colistine,
                                       Praticien=Praticien)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Microbiologie/ajouterPseudomonas.html', d)


def listeDemandePseudomonas(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Microbiologie.filter(nom__contains='pseudomonas')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Microbiologie/Pseudomonas.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Microbiologie/Pseudomonas.html', e)


@login_required(login_url='PageAuthentification')
def voirPseudomonas(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    pseudomonas = Pseudomonas.objects.all()
    d = {'pseudomonas': pseudomonas}
    return render(request, 'resultat/Microbiologie/listePseudomonas.html', d)


def ajouterResultat_Entérobactéries(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Fosfomycine = request.POST['Fosfomycine']
        Acide_nalid = request.POST['Acide_nalid']
        Trime_sulfam = request.POST['Trime_sulfam']
        Ciprofloxacine = request.POST['Ciprofloxacine']
        Furanes = request.POST['Furanes']
        Chloram = request.POST['Chloram']
        Colistine = request.POST['Colistine']
        Getamicine = request.POST['Getamicine']
        Amikacine = request.POST['Amikacine']
        Ertapéneme = request.POST['Ertapéneme']
        Imipéneme = request.POST['Imipéneme']
        Céfrazidime = request.POST['Céfrazidime']
        Aztréonam = request.POST['Aztréonam']
        Cefo_Ceftria = request.POST['Cefo_Ceftria']
        Cefoxitine = request.POST['Cefoxitine']
        Cefazoline = request.POST['Cefazoline']
        Amoxi_Acide = request.POST['Amoxi_Acide']
        Ampi_amo = request.POST['Ampi_amo']
        Praticien = request.POST['Praticien']
        try:

            Entérobactéries.objects.create(id_demande=pk, Fosfomycine=Fosfomycine, Acide_nalid=Acide_nalid,
                                           Trime_sulfam=Trime_sulfam,
                                           Ciprofloxacine=Ciprofloxacine, Furanes=Furanes, Chloram=Chloram,
                                           Colistine=Colistine, Getamicine=Getamicine, Amikacine=Amikacine,
                                           Ertapéneme=Ertapéneme, Imipéneme=Imipéneme, Céfrazidime=Céfrazidime,
                                           Aztréonam=Aztréonam, Cefo_Ceftria=Cefo_Ceftria, Cefoxitine=Cefoxitine,
                                           Cefazoline=Cefazoline, Amoxi_Acide=Amoxi_Acide, Ampi_amo=Ampi_amo,
                                           Praticien=Praticien)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Microbiologie/ajouterEntérobactéries.html', d)


def listeDemandeEntérobactéries(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Microbiologie.filter(nom__contains='Entérobactéries')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Microbiologie/Entérobactéries.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Microbiologie/Entérobactéries.html', e)


@login_required(login_url='PageAuthentification')
def voirEntérobactéries(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    entérobactéries = Entérobactéries.objects.all()
    d = {'entérobactéries': entérobactéries}
    return render(request, 'resultat/Microbiologie/listeEntérobactéries.html', d)


def ajouterResultat_Stapylocoque(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Penicilline = request.POST['Penicilline']
        Oxacilline = request.POST['Oxacilline']
        Cefoxitine = request.POST['Cefoxitine']
        Amikacine = request.POST['Amikacine']
        Gentamicine = request.POST['Gentamicine']
        Kanamycine = request.POST['Kanamycine']
        Eryth_Azith = request.POST['Eryth_Azith']
        Clind_linc = request.POST['Clind_linc']
        Prist_Quin_dal = request.POST['Prist_Quin_dal']
        Ofloxacine = request.POST['Ofloxacine']
        Ciprofloxacine = request.POST['Ciprofloxacine']
        Lévofloxacine = request.POST['Lévofloxacine']
        Chloram = request.POST['Chloram']
        Vancomycine = request.POST['Vancomycine']
        Rifampicine = request.POST['Rifampicine']
        Trime_sulfam = request.POST['Trime_sulfam']
        Tetracy_doxy = request.POST['Tetracy_doxy']
        Acidefucidique = request.POST['Acidefucidique']
        try:

            Stapylocoque.objects.create(id_demande=pk, Penicilline=Penicilline, Oxacilline=Oxacilline,
                                        Cefoxitine=Cefoxitine,
                                        Amikacine=Amikacine, Gentamicine=Gentamicine, Kanamycine=Kanamycine,
                                        Eryth_Azith=Eryth_Azith, Clind_linc=Clind_linc, Prist_Quin_dal=Prist_Quin_dal,
                                        Ofloxacine=Ofloxacine, Ciprofloxacine=Ciprofloxacine,
                                        Lévofloxacine=Lévofloxacine, Chloram=Chloram, Vancomycine=Vancomycine,
                                        Rifampicine=Rifampicine,
                                        Trime_sulfam=Trime_sulfam, Tetracy_doxy=Tetracy_doxy,
                                        Acidefucidique=Acidefucidique)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Microbiologie/ajouterStapylocoque.html', d)


def listeDemandeStapylocoque(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Microbiologie.filter(nom__contains='Stapylocoque')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Microbiologie/Stapylocoque.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Microbiologie/Stapylocoque.html', e)


@login_required(login_url='PageAuthentification')
def voirStapylocoque(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    stapylocoque = Stapylocoque.objects.all()
    d = {'stapylo': stapylocoque}
    return render(request, 'resultat/Microbiologie/listeStapylocoque.html', d)


def ajouterResultat_Acinetobacter(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Ticarcilline = request.POST['Ticarcilline']
        Piperacilline = request.POST['Piperacilline']
        Ticar_Acide = request.POST['Ticar_Acide']
        Ceftazidime = request.POST['Ceftazidime']
        Imipéneme = request.POST['Imipéneme']
        Amikacine = request.POST['Amikacine']
        Gentamicine = request.POST['Gentamicine']
        Tobramycine = request.POST['Tobramycine']
        Netilmicine = request.POST['Netilmicine']
        Ciprof = request.POST['Ciprof']
        Lévofloxamine = request.POST['Lévofloxamine']
        Tetracy_doxy = request.POST['Tetracy_doxy']
        Trime_sulfam = request.POST['Trime_sulfam']
        Colistine = request.POST['Colistine']
        Praticie = request.POST['Praticie']

        try:

            Acinetobacter.objects.create(id_demande=pk, Ticarcilline=Ticarcilline, Piperacilline=Piperacilline,
                                         Ticar_Acide=Ticar_Acide,
                                         Ceftazidime=Ceftazidime, Imipéneme=Imipéneme, Amikacine=Amikacine,
                                         Gentamicine=Gentamicine, Tobramycine=Tobramycine, Netilmicine=Netilmicine,
                                         Ciprof=Ciprof, Lévofloxamine=Lévofloxamine, Tetracy_doxy=Tetracy_doxy,
                                         Trime_sulfam=Trime_sulfam, Colistine=Colistine, Praticie=Praticie)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Microbiologie/ajouterAcinetobacter.html', d)


def listeDemandeAcinetobacter(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Microbiologie.filter(nom__contains='Acinetobacter')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Microbiologie/Acinetobacter.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Microbiologie/Acinetobacter.html', e)


@login_required(login_url='PageAuthentification')
def voirAcinetobacter(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    acinetobacter = Acinetobacter.objects.all()
    d = {'acinetobacter': acinetobacter}
    return render(request, 'resultat/Microbiologie/listeAcinetobacter.html', d)


########################################   Unité Biochimie   ###############################


def ajouterResultat_BilanDurgence(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Taux_pro = request.POST['Taux_pro']
        INR = request.POST['INR']
        Temp_cépha = request.POST['Temp_cépha']
        Glucose = request.POST['Glucose']
        Urée = request.POST['Urée']
        créatinine = request.POST['créatinine']
        Bilirubine = request.POST['Bilirubine']
        Calcium = request.POST['Calcium']
        CRP = request.POST['CRP']
        WBC = request.POST['WBC']
        RBC = request.POST['RBC']
        HGB = request.POST['HGB']
        HCT = request.POST['HCT']
        MCV = request.POST['MCV']
        MCH = request.POST['MCH']
        MCHC = request.POST['MCHC']
        PLT = request.POST['PLT']
        LYM = request.POST['LYM']
        NEUT = request.POST['NEUT']

        try:

            BilanDurgence.objects.create(id_demande=pk, Taux_pro=Taux_pro, INR=INR, Temp_cépha=Temp_cépha,
                                         Glucose=Glucose, Urée=Urée, créatinine=créatinine, Bilirubine=Bilirubine,
                                         Calcium=Calcium, CRP=CRP,
                                         WBC=WBC, RBC=RBC, HGB=HGB, HCT=HCT, MCV=MCV, MCH=MCH, MCHC=MCHC, PLT=PLT,
                                         LYM=LYM, NEUT=NEUT)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Biochimie/ajouterBilanDurgence.html', d)


def listeDemandeBilanDurgence(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Biochimie.filter(nom__contains='BilanDurgence')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Biochimie/BilanDurgence.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Biochimie/BilanDurgence.html', e)


@login_required(login_url='PageAuthentification')
def voirBilanDurgence(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    bilanDurgence = BilanDurgence.objects.all()
    d = {'bilanDurgence': bilanDurgence}
    return render(request, 'resultat/Biochimie/listeBilanDurgence.html', d)


def ajouterResultat_BiochimieGénérale(request, pk):
    demandeAnalyse = Demande.objects.get(id=pk)
    error = ""

    if not request.user.is_active:
        return redirect('PageAuthentification')

    if request.method == 'POST':
        Glucose = request.POST['Glucose']
        Urée = request.POST['Urée']
        Créatinine = request.POST['Créatinine']
        Acide_Urique = request.POST['Acide_Urique']
        Sodium = request.POST['Sodium']
        Potassium = request.POST['Potassium']
        Clicium_total = request.POST['Clicium_total']
        Calcium_ionisé = request.POST['Calcium_ionisé']
        Phosphore = request.POST['Phosphore']
        Magnésium = request.POST['Magnésium']
        Fer = request.POST['Fer']
        aspect_résum = request.POST['aspect_résum']
        Cholestérol_total = request.POST['Cholestérol_total']
        Triglycérides = request.POST['Triglycérides']
        HDL = request.POST['HDL']
        LDL = request.POST['LDL']
        Protéines = request.POST['Protéines']
        Albumine = request.POST['Albumine']
        Amylase = request.POST['Amylase']
        Lipase = request.POST['Lipase']
        CK_total = request.POST['CK_total']
        CK_Mb = request.POST['CK_Mb']
        LDH = request.POST['LDH']
        GOT = request.POST['GOT']
        GPT = request.POST['GPT']
        PAL = request.POST['PAL']
        y_gt = request.POST['y_gt']
        Bilirubine = request.POST['Bilirubine']
        Praticien = request.POST['Praticien']

        try:

            BiochimieGénérale.objects.create(id_demande=pk, Glucose=Glucose, Urée=Urée, Créatinine=Créatinine,
                                             Acide_Urique=Acide_Urique, Sodium=Sodium, Potassium=Potassium,
                                             Clicium_total=Clicium_total, Calcium_ionisé=Calcium_ionisé,
                                             Phosphore=Phosphore,
                                             Magnésium=Magnésium, Fer=Fer, aspect_résum=aspect_résum,
                                             Cholestérol_total=Cholestérol_total, Triglycérides=Triglycérides, HDL=HDL,
                                             LDL=LDL, Protéines=Protéines, Albumine=Albumine, Amylase=Amylase,
                                             Lipase=Lipase, CK_total=CK_total, CK_Mb=CK_Mb, LDH=LDH, GOT=GOT,
                                             GPT=GPT, PAL=PAL, y_gt=y_gt, Bilirubine=Bilirubine, Praticien=Praticien)
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error, 'demandeAnalyse': demandeAnalyse}
    return render(request, 'resultat/Biochimie/ajouterBiochimieGénérale.html', d)


def listeDemandeBiochimieGénérale(request):
    error = ""
    if not request.user.is_active:
        return redirect('PageAuthentification')

    demande = Demande.objects.all()
    listedemande = []
    for emende in demande:
        listedem = emende.Biochimie.filter(nom__contains='BiochimieGénérale')
        if listedem:
            listedemande.append(emende)

    if listedemande:
        d = {'listedemande': listedemande}
        error = "no"
        return render(request, 'resultat/Biochimie/BiochimieGénérale.html', d)
    else:
        error = "yes"
        e = {'error': error}
        return render(request, 'resultat/Biochimie/BiochimieGénérale.html', e)


@login_required(login_url='PageAuthentification')
def voirBiochimieGénérale(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    biochimieGénérale = BiochimieGénérale.objects.all()
    d = {'biochimieGénérale': biochimieGénérale}
    return render(request, 'resultat/Biochimie/listeBiochimieGénérale.html', d)


def listeAnalyse(request, pk):
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()

    d = {'analyseBiochimie': analyseBiochimie, 'demande': demande, 'analyseParasitologie': analyseParasitologie,
         'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
    return render(request, 'resultat/analyseDamander.html', d)


def consulterResultat(request, pk):
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()

    d = {'analyseBiochimie': analyseBiochimie, 'demande': demande, 'analyseParasitologie': analyseParasitologie,
         'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
    return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatCoproparasitologie(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = coproparasitologie.objects.all().filter(id_demande__iexact=pk)

    if co:
        copro = coproparasitologie.objects.get(id_demande=pk)
        d = {'copro': copro, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Parasitologie/VoirResultatCopro.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatEntérocoque(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = Entérocoque.objects.all().filter(id_demande__iexact=pk)

    if co:
        entero = Entérocoque.objects.get(id_demande=pk)
        d = {'entero': entero, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Parasitologie/VoirResultatEntero.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatbactériologie(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = bactériologie.objects.all().filter(id_demande__iexact=pk)

    if co:
        bacterio = bactériologie.objects.get(id_demande=pk)
        d = {'bacterio': bacterio, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Parasitologie/VoirResultatbacterio.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatStapylocoque(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = Stapylocoque.objects.all().filter(id_demande__iexact=pk)

    if co:
        stapylo = Stapylocoque.objects.get(id_demande=pk)
        d = {'stapylo': stapylo, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Microbiologie/VoirResultatstapylo.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatEntérobactéries(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = Entérobactéries.objects.all().filter(id_demande__iexact=pk)

    if co:
        entero = Entérobactéries.objects.get(id_demande=pk)
        d = {'entero': entero, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Microbiologie/VoirResultatentero.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatPseudomonas(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = Pseudomonas.objects.all().filter(id_demande__iexact=pk)

    if co:
        pseudo = Pseudomonas.objects.get(id_demande=pk)
        d = {'pseudo': pseudo, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Microbiologie/VoirResultatpseudo.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatAcinetobacter(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = Acinetobacter.objects.all().filter(id_demande__iexact=pk)

    if co:
        acineto = Acinetobacter.objects.get(id_demande=pk)
        d = {'acineto': acineto, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Microbiologie/VoirResultatacineto.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatFNS(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = FNS.objects.all().filter(id_demande__iexact=pk)

    if co:
        fns = FNS.objects.get(id_demande=pk)
        d = {'fns': fns, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Hémobiologie/VoirResultatfns.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatGroupageSanguin(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = groupageSanguin.objects.all().filter(id_demande__iexact=pk)

    if co:
        groupe = groupageSanguin.objects.get(id_demande=pk)
        d = {'groupe': groupe, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Hémobiologie/VoirResultatgroupe.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatBilanDurgence(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = BilanDurgence.objects.all().filter(id_demande__iexact=pk)

    if co:
        bilan = BilanDurgence.objects.get(id_demande=pk)
        d = {'bilan': bilan, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Biochimie/VoirResultatbilan.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


def voirResultatBiochimieGénérale(request, pk):
    erreur = ""
    demande = Demande.objects.get(id=pk)
    analyseBiochimie = demande.Biochimie.all()
    analyseParasitologie = demande.Parasitologie.all()
    analyseMicrobiologie = demande.Microbiologie.all()
    analyseHémobiologie = demande.Hémobiologie.all()
    demande = Demande.objects.get(id=pk)
    co = BiochimieGénérale.objects.all().filter(id_demande__iexact=pk)

    if co:
        bioc = BiochimieGénérale.objects.get(id_demande=pk)
        d = {'bioc': bioc, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/Biochimie/VoirResultatbioc.html', d)
    else:
        erreur = "yes"
        d = {'erreur': erreur, 'demande': demande, 'analyseBiochimie': analyseBiochimie, 'demande': demande,
             'analyseParasitologie': analyseParasitologie,
             'analyseMicrobiologie': analyseMicrobiologie, 'analyseHémobiologie': analyseHémobiologie}
        return render(request, 'resultat/ResultatDamander.html', d)


################## Supprimer Resultat ###########################

def supprimerResultatCoproparasitologie(request, pk):
    copro = coproparasitologie.objects.get(id=pk)
    if request.method == 'POST':
        copro.delete()
        return redirect('listeCopro')
    context = {'item': copro}
    return render(request, 'resultat/Parasitologie/supprimercopro.html', context)


def supprimerResultatBactériologie(request, pk):
    bacterio = bactériologie.objects.get(id=pk)
    if request.method == 'POST':
        bacterio.delete()
        return redirect('listebacterio')
    context = {'item': bacterio}
    return render(request, 'resultat/Parasitologie/supprimerbacterio.html', context)


def supprimerResultatEntérocoque(request, pk):
    entero = Entérocoque.objects.get(id=pk)
    if request.method == 'POST':
        entero.delete()
        return redirect('listeEntérocoque')
    context = {'item': entero}
    return render(request, 'resultat/Parasitologie/supprimerenteroco.html', context)


def supprimerResultatGroupageSanguin(request, pk):
    groupe = groupageSanguin.objects.get(id=pk)
    if request.method == 'POST':
        groupe.delete()
        return redirect('listeGroupageSanguin')
    context = {'item': groupe}
    return render(request, 'resultat/Hémobiologie/supprimergroupe.html', context)


def supprimerResultatFNS(request, pk):
    fns = FNS.objects.get(id=pk)
    if request.method == 'POST':
        fns.delete()
        return redirect('listeFNS')
    context = {'item': fns}
    return render(request, 'resultat/Hémobiologie/supprimerfns.html', context)


def supprimerResultatPseudomonas(request, pk):
    pseudo = Pseudomonas.objects.get(id=pk)
    if request.method == 'POST':
        pseudo.delete()
        return redirect('listePseudomonas')
    context = {'item': pseudo}
    return render(request, 'resultat/Microbiologie/supprimerpseudo.html', context)


def supprimerResultatEntérobactéries(request, pk):
    entero = Entérobactéries.objects.get(id=pk)
    if request.method == 'POST':
        entero.delete()
        return redirect('listeEntérobactéries')
    context = {'item': entero}
    return render(request, 'resultat/Microbiologie/supprimerentero.html', context)


def supprimerResultatStapylocoque(request, pk):
    stapylo = Stapylocoque.objects.get(id=pk)
    if request.method == 'POST':
        stapylo.delete()
        return redirect('listeStapylocoque')
    context = {'item': stapylo}
    return render(request, 'resultat/Microbiologie/supprimerstapylo.html', context)


def supprimerResultatAcinetobacter(request, pk):
    acinito = Acinetobacter.objects.get(id=pk)
    if request.method == 'POST':
        acinito.delete()
        return redirect('listeAcinetobacter')
    context = {'item': acinito}
    return render(request, 'resultat/Microbiologie/supprimeracinito.html', context)


def supprimerResultatBiochimieGénérale(request, pk):
    bioc = BiochimieGénérale.objects.get(id=pk)
    if request.method == 'POST':
        bioc.delete()
        return redirect('listeBiochimieGénérale')
    context = {'item': bioc}
    return render(request, 'resultat/Biochimie/supprimerbioc.html', context)


def supprimerResultatBilanDurgence(request, pk):
    bilan = BilanDurgence.objects.get(id=pk)
    if request.method == 'POST':
        bilan.delete()
        return redirect('listeBilanDurgence')
    context = {'item': bilan}
    return render(request, 'resultat/Biochimie/supprimerbilan.html', context)


################################################ Modifier Resultat ########################################
def modifierResultatCopro(request, pk):
    copro = coproparasitologie.objects.get(id=pk)
    form = CoproForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = CoproForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeCopro')

    context = {'form': form}
    return render(request, 'resultat/Parasitologie/modifierCopro.html', context)


def modifierResultatBactériologie(request, pk):
    copro = bactériologie.objects.get(id=pk)
    form = BactériologieForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = BactériologieForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeBacterio')

    context = {'form': form}
    return render(request, 'resultat/Parasitologie/modifierbacterio.html', context)


def modifierResultatEntérocoque(request, pk):
    copro = Entérocoque.objects.get(id=pk)
    form = EntérocoqueForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = EntérocoqueForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeEntérocoque')

    context = {'form': form}
    return render(request, 'resultat/Parasitologie/modifierEntéro.html', context)


def modifierResultatGroupageSanguin(request, pk):
    copro = groupageSanguin.objects.get(id=pk)
    form = GroupeForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = GroupeForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeGroupageSanguin')

    context = {'form': form}
    return render(request, 'resultat/Hémobiologie/modifierGroupe.html', context)


def modifierResultatFNS(request, pk):
    copro = FNS.objects.get(id=pk)
    form = FNSForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = FNSForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeFNS')
    context = {'form': form}
    return render(request, 'resultat/Hémobiologie/modifierFNS.html', context)


def modifierResultatPseudomonas(request, pk):
    copro = Pseudomonas.objects.get(id=pk)
    form = PseudoForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = PseudoForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listePseudomonas')

    context = {'form': form}
    return render(request, 'resultat/Microbiologie/modifierPseudo.html', context)


def modifierResultatEntérobactéries(request, pk):
    copro = Entérobactéries.objects.get(id=pk)
    form = EntérobactériesForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = EntérobactériesForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeEntérobactéries')

    context = {'form': form}
    return render(request, 'resultat/Microbiologie/modifierEntéro.html', context)


def modifierResultatStapylocoque(request, pk):
    copro = Stapylocoque.objects.get(id=pk)
    form = StapyloForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = StapyloForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeStapylocoque')

    context = {'form': form}
    return render(request, 'resultat/Microbiologie/modifierStapylo.html', context)


def modifierResultatAcinetobacter(request, pk):
    copro = Acinetobacter.objects.get(id=pk)
    form = AcinetoForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = AcinetoForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeAcinetobacter')

    context = {'form': form}
    return render(request, 'resultat/Microbiologie/modifierAcineto.html', context)


def modifierResultatBiochimieGénérale(request, pk):
    copro = BiochimieGénérale.objects.get(id=pk)
    form = BiocForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = BiocForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeBiochimieGénérale')

    context = {'form': form}
    return render(request, 'resultat/Biochimie/modifierBioc.html', context)


def modifierResultatBilanDurgence(request, pk):
    copro = BilanDurgence.objects.get(id=pk)
    form = BilanForm(instance=copro)
    if request.method == 'POST':  # quand je click sur envoyer j'enregiste les modifs
        form = BilanForm(request.POST, instance=copro)
        if form.is_valid():
            form.save()
            return redirect('listeBilanDurgence')

    context = {'form': form}
    return render(request, 'resultat/Biochimie/modifierBilan.html', context)



def AfficherResultatGroupeSanguin(request, pk):
    try:
        groupe = groupageSanguin.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = groupe.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'groupe': groupe, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Hémobiologie/Resultatgroupe.html', d)


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


from django.core.mail import EmailMultiAlternatives


def EnvoyerResultatGroupeSanguin(request, pk):
    try:
        groupe = groupageSanguin.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = groupe.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'groupe': groupe, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Hémobiologie/ImprimerGrp.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Analyse Groupe Sanguin CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Hémobiologie/ImprimerGrp.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': groupe})
        else:
            pas = demande.nomPatient

            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Hémobiologie/ImprimerGrp.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': groupe})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': groupe})


def AfficherResultatBacterio(request, pk):
    try:
        bac = bactériologie.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = bac.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'bac': bac, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Parasitologie/Resultatbacterio.html', d)


def EnvoyerResultatBacterio(request, pk):
    try:
        bac = bactériologie.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = bac.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'bac': bac, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Parasitologie/Envoyerbacterio.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Analyse Bactériologie CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Parasitologie/Envoyerbacterio.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': bac})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Parasitologie/Envoyerbacterio.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': bac})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': bac})


def AfficherResultatCopro(request, pk):
    try:
        copro = coproparasitologie.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = copro.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'copro': copro, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Parasitologie/ResultatCopro.html', d)


def EnvoyerResultatCopro(request, pk):
    try:
        copro = bactériologie.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = copro.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'copro': copro, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Parasitologie/Envoyerbacterio.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Analyse Coproparasitologie CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Parasitologie/EnvoyerCopro.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': copro})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Parasitologie/EnvoyerCopro.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': copro})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': copro})


def AfficherResultatEntérocoque(request, pk):
    try:
        ent = Entérocoque.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = ent.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'ent': ent, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Parasitologie/ResultatEntero.html', d)


def EnvoyerResultatEntérocoque(request, pk):
    try:
        ent = Entérocoque.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = ent.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'ent': ent, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Parasitologie/EnvoyerEntero.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Analyse Entérocoque CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Parasitologie/EnvoyerCopro.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': ent})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Parasitologie/EnvoyerEntero.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': ent})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': ent})


def AfficherResultatFNS(request, pk):
    try:
        fns = FNS.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = fns.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'fns': fns, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Hémobiologie/Resultatfns.html', d)


def EnvoyerResultatFNS(request, pk):
    try:
        fns = FNS.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = fns.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'fns': fns, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Hémobiologie/EnvoyerFNS.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Analyse FNS CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Hémobiologie/EnvoyerFNS.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': fns})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Hémobiologie/EnvoyerFNS.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': fns})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': fns})


def AfficherResultatPseudomonas(request, pk):
    try:
        ps = Pseudomonas.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = ps.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'ps': ps, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Microbiologie/Resultatpseudo.html', d)


def EnvoyerResultatPseudomonas(request, pk):
    try:
        ps = Pseudomonas.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = ps.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'ps': ps, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Microbiologie/EnvoyerPseudo.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Analyse Pseudomonas CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Microbiologie/EnvoyerPseudo.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': ps})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Microbiologie/EnvoyerPseudo.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': ps})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': ps})


def AfficherResultatEntérobactéries(request, pk):
    try:
        entbac = Entérobactéries.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = entbac.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'entbac': entbac, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Microbiologie/Resultatentero.html', d)


def EnvoyerResultatEntérobactéries(request, pk):
    try:
        entbac = Entérobactéries.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = entbac.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'entbac': entbac, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Microbiologie/EnvoyerEnterbac.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Analyse Entébactéries CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Microbiologie/EnvoyerEnterbac.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': entbac})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Microbiologie/EnvoyerEnterbac.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': entbac})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': entbac})


def AfficherResultatStapylocoque(request, pk):
    try:
        s = Stapylocoque.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = s.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'s': s, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Microbiologie/Resultatstapylo.html', d)


def EnvoyerResultatStapylocoque(request, pk):
    try:
        s = Stapylocoque.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = s.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'s': s, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Microbiologie/EnvoyerStap.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Analyse Stapylocoque CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Microbiologie/EnvoyerStap.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': s})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Microbiologie/EnvoyerStap.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': s})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': s})


def AfficherResultatBiochimieGenerale(request, pk):
    try:
        bio = BiochimieGénérale.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = bio.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'bio': bio, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Biochimie/Resultatbioc.html', d)


def EnvoyerResultatBiochimieGenerale(request, pk):
    try:
        bio = BiochimieGénérale.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = bio.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'bio': bio, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Biochimie/EnvoyerBiog.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Biochimie CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Biochimie/EnvoyerBiog.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': bio})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Biochimie/EnvoyerBiog.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': bio})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': bio})


def AfficherResultatBilanDurgence(request, pk):
    try:
        bilan = BilanDurgence.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = bilan.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'bilan': bilan, 'idDemande': idDemande, 'demande': demande}
    return render(request, 'resultat/Biochimie/Resultatbilan.html', d)


def EnvoyerResultatBilanDurgence(request, pk):
    try:
        bilan = BilanDurgence.objects.get(id=pk)
    except:
        return HttpResponse("505 not trouver")
    idDemande = bilan.id_demande
    demande = Demande.objects.get(id=idDemande)
    d = {'bilan': bilan, 'idDemande': idDemande, 'demande': demande}
    template = get_template('resultat/Biochimie/EnvoyerBilan.html')
    html = template.render(d)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    pdf = result.getvalue()
    filename = demande.nomPatient + "  " + demande.prenomPatient + '_CHU DOUERA' + '.pdf'
    mail_subject = 'Resultat Bilan Urgence CHU DOUERA'
    service = demande.service
    try:
        if service not in 'Externe':
            user = Service.objects.get(nomService=service)
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Biochimie/EnvoyerBilan.html')
            message = template.render(context_dict)
            to_email = user.email
            message = 'Bonjour' + ' ' + demande.Nommedecin_demandeur + ' ' \
                      + demande.Prenommedecin_demandeur + ' ,Voici ci joint votre Resultat analyse.'
            # for including css(only inline css works) in mail and remove autoescape off
            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': bilan})
        else:
            pas = demande.nomPatient
            pasp = demande.prenomPatient
            pasbdd = Patient.objects.get(nom=pas, prenom=pasp)
            user = pasbdd.email
            context_dict = {
                'user': user,
                'demande': demande
            }
            template = get_template('resultat/Biochimie/EnvoyerBilan.html')
            message = template.render(context_dict)
            to_email = user
            message = 'Bonjour' + ' ' + demande.nomPatient + ' ' + demande.prenomPatient \
                      + ',Voici ci joint votre Resultat analyse.'

            email = EmailMultiAlternatives(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email]
            )
            email.attach_alternative(message, "text/html")
            email.attach(filename, pdf, 'application/pdf')
            email.send(fail_silently=False)
            return render(request, 'resultat/Hémobiologie/SucessEmail.html', {'id': idDemande, 'groupe': bilan})
    except:
        return render(request, 'resultat/Hémobiologie/FailEmail.html', {'id': idDemande, 'groupe': bilan})

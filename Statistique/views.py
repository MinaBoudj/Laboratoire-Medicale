from django.shortcuts import render, redirect
from Patient.models import *
from Analyse.models import *
from Resultat.models import *
from django.db.models import Q
from Analyse.forms import *
import datetime


def Statistique(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')

    listeDemandeanalyse = Demande.objects.all()
    total_demande = listeDemandeanalyse.count()

    d = {
        'total_demande': total_demande, 'listeDemandeanalyse': listeDemandeanalyse,

    }
    return render(request, 'statistique/AjouterStatistique.html', d)


def Stat(request):
    if request.method == 'POST':
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        list1 = Demande.objects.all()
        result = list1.filter(date_ajout_demande__lte=todate,
                              date_ajout_demande__gte=fromdate)
        d = {'result': result, 'fromdate': fromdate, 'todate': todate, 'list': list1}
        return render(request, 'statistique/Ajouter.html', d)
    else:
        return render(request, 'statistique/Ajouter.html')


def ServiceStat(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    listeDemandeanalyse = Demande.objects.all()
    total_demande = listeDemandeanalyse.count()
    POA = listeDemandeanalyse.filter(service='POA').count()
    POB = listeDemandeanalyse.filter(service='POB').count()
    COA = listeDemandeanalyse.filter(service='COA').count()
    Externe = listeDemandeanalyse.filter(service='Externe').count()
    ListePOA = listeDemandeanalyse.filter(service='POA')
    ListePOB = listeDemandeanalyse.filter(service='POB')
    ListeCOA = listeDemandeanalyse.filter(service='COA')
    ListeExterne = listeDemandeanalyse.filter(service='Externe')
    d = {'listeDemandeanalyse': listeDemandeanalyse, 'total_demande': total_demande, 'POA': POA,
         'POB': POB,
         'COA': COA, 'Externe': Externe, 'ListePOA': ListePOA, 'ListePOB': ListePOB, 'ListeCOA': ListeCOA,
         'ListeExterne': ListeExterne, }
    return render(request, 'statistique/service.html', d)


def BiochimieStat(request):
    biochimieGénérale = BiochimieGénérale.objects.all()
    bio = biochimieGénérale.count()
    bilanDurgence = BilanDurgence.objects.all()
    b = bilanDurgence.count()
    d = {'bilanDurgence': bilanDurgence, 'bilanDurgence': bilanDurgence, 'b': b, 'bio': bio}
    return render(request, 'Statistique/Biochimie/bio.html', d)


def ParasitologieStat(request):
    Coproparasitologie = coproparasitologie.objects.all()
    c = Coproparasitologie.count()
    Bactériologie = bactériologie.objects.all()
    bac = Bactériologie.count()
    entérocoque = Entérocoque.objects.all()
    ent = entérocoque.count()
    d = {'Coproparasitologie': Coproparasitologie,
         'Bactériologie': Bactériologie, 'c': c, 'bac': bac, 'ent': ent}
    return render(request, 'Statistique/Parasitologie/para.html', d)


def MicrobiologieStat(request):
    pseudomonas = Pseudomonas.objects.all()
    p = pseudomonas.count()
    entérobactéries = Entérobactéries.objects.all()
    e = entérobactéries.count()
    stapylocoque = Stapylocoque.objects.all()
    s = stapylocoque.count()

    d = {'pseudomonas': pseudomonas, 'entérobactéries': entérobactéries,
         'stapylocoque': stapylocoque, 'p': p, 'e': e, 's': s}
    return render(request, 'Statistique/Microbiologie/Micro.html', d)


def HemobiologieStat(request):
    GroupageSanguin = groupageSanguin.objects.all()
    g = GroupageSanguin.count()
    fNS = FNS.objects.all()
    f = fNS.count()

    d = {'fNS': fNS, 'f': f, 'g': g}
    return render(request, 'Statistique/Hemobiologie/Hemo.html', d)


def StatistiquePatient(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')

    listePatient = Patient.objects.all()
    total_patient = listePatient.count()
    listeDemandeanalyse = Demande.objects.all()

    result1 = listeDemandeanalyse.filter(age__gte=0, age__lte=5,service='POA').count()
    result2 = listeDemandeanalyse.filter(age__gte=6, age__lte=10,service='POA').count()
    result3 = listeDemandeanalyse.filter(age__gte=11, age__lte=15,service='POA').count()
    result4 = listeDemandeanalyse.filter(age__gte=15 , age__lte=20,service='POA').count()
    result5 = listeDemandeanalyse.filter(age__gte=21, age__lte=25,service='POA').count()
    result6 = listeDemandeanalyse.filter(age__gte=26, age__lte=30,service='POA').count()
    result7 = listeDemandeanalyse.filter(age__gte=31, age__lte=40,service='POA').count()
    result8 = listeDemandeanalyse.filter(age__gte=41, age__lte=45,service='POA').count()
    result9 = listeDemandeanalyse.filter(age__gte=46, age__lte=50,service='POA').count()
    result10 = listeDemandeanalyse.filter(age__gte=51, age__lte=55,service='POA').count()
    result11 = listeDemandeanalyse.filter(age__gte=56, age__lte=60,service='POA').count()
    result12 = listeDemandeanalyse.filter(age__gte=61, age__lte=70,service='POA').count()
    result13 = listeDemandeanalyse.filter(age__gte=71, age__lte=80,service='POA').count()
    result14 = listeDemandeanalyse.filter(age__gte=81, age__lte=100,service='POA').count()

    Sresult1 = listeDemandeanalyse.filter(age__gte=0, age__lte=5, service='POA').count()
    Sresult2 = listeDemandeanalyse.filter(age__gte=6, age__lte=10, service='POB').count()
    Sresult3 = listeDemandeanalyse.filter(age__gte=11, age__lte=15, service='POB').count()
    Sresult4 = listeDemandeanalyse.filter(age__gte=15, age__lte=20, service='POB').count()
    Sresult5 = listeDemandeanalyse.filter(age__gte=21, age__lte=25, service='POB').count()
    Sresult6 = listeDemandeanalyse.filter(age__gte=26, age__lte=30, service='POB').count()
    Sresult7 = listeDemandeanalyse.filter(age__gte=31, age__lte=40, service='POB').count()
    Sresult8 = listeDemandeanalyse.filter(age__gte=41, age__lte=45, service='POB').count()
    Sresult9 = listeDemandeanalyse.filter(age__gte=46, age__lte=50, service='POB').count()
    Sresult10 = listeDemandeanalyse.filter(age__gte=51, age__lte=55, service='POB').count()
    Sresult11 = listeDemandeanalyse.filter(age__gte=56, age__lte=60, service='POB').count()
    Sresult12 = listeDemandeanalyse.filter(age__gte=61, age__lte=70, service='POB').count()
    Sresult13 = listeDemandeanalyse.filter(age__gte=71, age__lte=80, service='POB').count()
    Sresult14 = listeDemandeanalyse.filter(age__gte=81, age__lte=100, service='POB').count()

    aSresult1 = listeDemandeanalyse.filter(age__gte=0, age__lte=5, service='COA').count()
    aSresult2 = listeDemandeanalyse.filter(age__gte=6, age__lte=10, service='COA').count()
    aSresult3 = listeDemandeanalyse.filter(age__gte=11, age__lte=15, service='COA').count()
    aSresult4 = listeDemandeanalyse.filter(age__gte=15, age__lte=20, service='COA').count()
    aSresult5 = listeDemandeanalyse.filter(age__gte=21, age__lte=25, service='COA').count()
    aSresult6 = listeDemandeanalyse.filter(age__gte=26, age__lte=30, service='COA').count()
    aSresult7 = listeDemandeanalyse.filter(age__gte=31, age__lte=40, service='COA').count()
    aSresult8 = listeDemandeanalyse.filter(age__gte=41, age__lte=45, service='COA').count()
    aSresult9 = listeDemandeanalyse.filter(age__gte=46, age__lte=50, service='COA').count()
    aSresult10 = listeDemandeanalyse.filter(age__gte=51, age__lte=55, service='COA').count()
    aSresult11 = listeDemandeanalyse.filter(age__gte=56, age__lte=60, service='COA').count()
    aSresult12 = listeDemandeanalyse.filter(age__gte=61, age__lte=70, service='COA').count()
    aSresult13 = listeDemandeanalyse.filter(age__gte=71, age__lte=80, service='COA').count()
    aSresult14 = listeDemandeanalyse.filter(age__gte=81, age__lte=100, service='COA').count()

    eSresult1 = listeDemandeanalyse.filter(age__gte=0, age__lte=5, service='Externe').count()
    eSresult2 = listeDemandeanalyse.filter(age__gte=6, age__lte=10, service='Externe').count()
    eSresult3 = listeDemandeanalyse.filter(age__gte=11, age__lte=15, service='Externe').count()
    eSresult4 = listeDemandeanalyse.filter(age__gte=15, age__lte=20, service='Externe').count()
    eSresult5 = listeDemandeanalyse.filter(age__gte=21, age__lte=25, service='Externe').count()
    eSresult6 = listeDemandeanalyse.filter(age__gte=26, age__lte=30, service='Externe').count()
    eSresult7 = listeDemandeanalyse.filter(age__gte=31, age__lte=40, service='Externe').count()
    eSresult8 = listeDemandeanalyse.filter(age__gte=41, age__lte=45, service='Externe').count()
    eSresult9 = listeDemandeanalyse.filter(age__gte=46, age__lte=50, service='Externe').count()
    eSresult10 = listeDemandeanalyse.filter(age__gte=51, age__lte=55, service='Externe').count()
    eSresult11 = listeDemandeanalyse.filter(age__gte=56, age__lte=60, service='Externe').count()
    eSresult12 = listeDemandeanalyse.filter(age__gte=61, age__lte=70, service='Externe').count()
    eSresult13 = listeDemandeanalyse.filter(age__gte=71, age__lte=80, service='Externe').count()
    eSresult14 = listeDemandeanalyse.filter(age__gte=81, age__lte=100, service='Externe').count()

    d = {
        'total_demande': total_patient, 'listeDemandeanalyse': listeDemandeanalyse, 'listePatient': listePatient,
        'result1': result1,
        'result2': result2, 'resul3': result3, 'result4': result4, 'result5': result5,
        'result6': result6, 'result7': result7, 'result8': result8, 'result9': result9,
        'result10': result10, 'result11': result11, 'result12': result12, 'result13': result13, 'result14': result14,
        'Sresult1': Sresult1,
        'Sresult2': Sresult2, 'Sresul3': Sresult3, 'Sresult4': Sresult4, 'Sresult5': Sresult5,
        'Sresult6': Sresult6, 'Sresult7': Sresult7, 'Sresult8': Sresult8, 'Sresult9': Sresult9,
        'Sresult10': Sresult10, 'Sresult11': Sresult11, 'Sresult12': Sresult12,
        'Sresult13': Sresult13, 'Sresult14': Sresult14,
        'aSresult1': aSresult1,
        'aSresult2': aSresult2, 'aSresul3': aSresult3, 'aSresult4': aSresult4, 'aSresult5': aSresult5,
        'aSresult6': aSresult6, 'aSresult7': aSresult7, 'aSresult8': aSresult8, 'aSresult9': aSresult9,
        'aSresult10': aSresult10, 'aSresult11': aSresult11, 'aSresult12': aSresult12,
        'aSresult13': aSresult13, 'aSresult14': aSresult14,
        'eSresult1': eSresult1,
        'eSresult2': eSresult2, 'eSresul3': eSresult3, 'eSresult4': eSresult4, 'eSresult5': eSresult5,
        'eSresult6': eSresult6, 'eSresult7': eSresult7, 'eSresult8': eSresult8, 'eSresult9': eSresult9,
        'eSresult10': eSresult10, 'eSresult11': eSresult11, 'eSresult12': eSresult12,
        'eSresult13': eSresult13, 'eSresult14': eSresult14,

    }
    return render(request, 'statistique/Patient/patient.html', d)

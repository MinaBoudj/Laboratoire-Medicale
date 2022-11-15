from django.db.models import query
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .forms import *
from .filters import Patientfilter
from django.core.paginator import Paginator,EmptyPage
from django.urls import reverse_lazy , reverse
from django.utils.http import urlencode
from Analyse.models import *



# Create your views here.



def AjouterPatient(request):
	error = ""

	if not request.user.is_active:
		return redirect('PageAuthentification')
	
	if request.method == 'POST':
		nom = request.POST['nom']
		prenom = request.POST['prenom']
		email = request.POST['email']
		genre = request.POST['genre']
		numTel = request.POST['numTel']
		adresse = request.POST['adresse']
		dateNaissance = request.POST['DateNaissance']
		groupeSanguin = request.POST['groupeSanguin']		
		
		try:
				Patient.objects.create(nom=nom,prenom=prenom,email=email,genre=genre,numTel=numTel,adresse=adresse,dateNaissance=dateNaissance,groupeSanguin=groupeSanguin)
				error = "no"
		except Exception as e:
			error = "yes"
	d = {'error' : error}
	return render(request,'patient/ajouterPatient.html',d)	
	
	 
def search(request): 
	erreur = ""
	query = request.GET["nomp"]
	queryp = request.GET['prenomp']
	nomPatient=Patient.objects.all().filter(nom__iexact=query)
	prenomPatient=Patient.objects.all().filter(prenom__iexact=queryp)
	if nomPatient:
		if prenomPatient:
			erreur = "no"
		else:
			erreur= "yes"	
	else:
		erreur = "yes"
	d = {'erreur':erreur}
	return render(request,'patient/ajouterPatient.html', d)		


@login_required(login_url='PageAuthentification')
def voirPatient(request):
	if not request.user.is_active:
		return redirect('PageAuthentification')
	
	patient = Patient.objects.all()
	d = { 'patient' : patient }
	return render(request,'patient/listPatient.html',d)

def listePatient(request):
	selected = "patients"
	liste_patient = Patient.objects.all()

	if request.method =='POST':
		form = PatientSearcForm(request.POST)
		if form.is_valid():
			base_url = reverse('patients')
			query_string = urlencode(form.cleaned_data)
			url ='{}?{}'.format(base_url,query_string)
			return redirect(url)
	else:
		
		form = PatientSearcForm()
		nom_form = request.GET.get("nom", "")
		prenom_form=request.GET.get("prenom", "")
		if nom_form is not None:
			liste_patient = liste_patient.filter(nom__icontains=nom_form)
			#form.fields['nom'].initial = nom_form
		if prenom_form is not None:
			liste_patient = liste_patient.filter(prenom__icontains=prenom_form)	
			#form.fields['prenom'].initial = prenom_form


	paginator = Paginator(liste_patient.order_by('-date_ajout'),10)
	try:
		page = request.GET.get("page")
		if not page:
			page=1
		liste_patient = paginator.page(page)
	except EmptyPage:
		liste_patient = paginator.page(paginator.num_pages())
	return render(request,'patient/listPatient.html',locals())			



def modifier_patient(request,pk):
    patient=Patient.objects.get(id=pk)
    form=PatientForm(instance=patient)

    if request.method=='POST':  #quand je click sur envoyer j'enregiste les modifs
	    form=PatientForm(request.POST, instance=patient)
	    if form.is_valid():
		     form.save()
		     return redirect('listePatient')
    context={'form':form}         
    return render(request, 'patient/formPatient.html',context) 


def supprimerPatient(request,pk,email):
	if not request.user.is_staff:
		return redirect('Connexion_Admin')
	patient=Patient.objects.get(id=pk)
	if request.method=='POST':
		patient.delete()
		users = User.objects.filter(username=email)
		users.delete()
		return redirect('listePatient') 
	context={'item':patient}
	return render(request, 'patient/supprimerPatient.html',context)    

def dossierPatient(request,pk):
	if not request.user.is_active:
		return redirect('PageAuthentification')

	patient=Patient.objects.get(id=pk)	
	
	liste_demandePatient=Demande.objects.all().filter(idPatient=pk)  
	context={'patient':patient,'liste_demandePatient':liste_demandePatient}
	return render(request,'patient/dossierPatient.html',context)		 
    




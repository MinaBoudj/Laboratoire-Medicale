from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from Biologiste.models import *
from Medecin.models import *
from Patient.models import *
from Receptionniste.models import *
from django.contrib import messages



# Create your views here.

def PageAuthentification(request):
	error = ""
	page = ""
	if request.method == 'POST':
		u = request.POST['email']
		p = request.POST['password']
		user = authenticate(request,username=u,password=p)
		
		try:
			if user is not None:
				login(request,user)
				error = "no"
				g = request.user.groups.all()[0].name
				if g == 'Medecin':
					page = "medecin"
					d = {'error': error,'page':page}
					return render(request,'medecin/pageMedecin.html',d)
				elif g == 'Receptionniste':
					page = "reception"
					d = {'error': error,'page':page}
					return render(request,'receptionniste/pageReception.html',d)
				elif g == 'Biologiste':
					page = "biologiste"
					d = {'error': error,'page':page}
					return render(request,'biologiste/pagebiologiste.html',d)
			else:
				error = "yes"
				messages.error(request, "E-mail ou Mot de passe est incorrect")
		except Exception as e:
			error = "yes"
			#print(e)
			#raise e
	d ={'error':error}		
	#return render(request,'connexion/pageAuthentification.html')
	return render(request,'connexion/pageAuthentification.html',d)



def Connexion_Admin(request):
	error = ""
	if request.method == 'POST':
		u = request.POST['username']
		p = request.POST['password']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error = "yes"
			messages.error(request, "Nom d'utilisateur ou Mot de passe est incorrect")
	d = {'error' : error}
	return render(request,'administrateur/AuthentificationAdmin.html',d)


def Deconnexion_admin(request):
	if not request.user.is_staff:
		return redirect('Connexion_Admin')
	logout(request)
	return redirect('Connexion_Admin')



def Deconnecter(request):
    logout(request)
    return redirect('PageAuthentification') 

def PageAdmin(request):
	#apres la connexion de l'administrateur il accéde a cette page
	if not request.user.is_staff:
		return redirect('Connexion_Admin')
	return render(request,'administrateur/pageAdministrateur.html')



def Profile(request):
	if not request.user.is_active:
		return redirect('PageAuthentification')

	g = request.user.groups.all()[0].name
	if g == 'Biologiste':
		biologiste_detials = Biologiste.objects.all().filter(email=request.user)
		d = { 'biologiste_detials' : biologiste_detials }
		return render(request,'biologiste/profileBiologiste.html',d)
	elif g == 'Medecin':
		medecin_detials = Medecin.objects.all().filter(email=request.user)
		d = { 'medecin_detials' : medecin_detials }
		return render(request,'medecin/profileMedecin.html',d)
	elif g == 'Receptionniste':
		reception_details = Receptionniste.objects.all().filter(email=request.user)
		d = { 'reception_details' : reception_details }
		return render(request,'receptionniste/profileReceptionniste.html',d)


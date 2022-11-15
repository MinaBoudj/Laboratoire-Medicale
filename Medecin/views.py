from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .forms import *

def AjouterMedecin(request):
    error = ""
    user = "none"

    if not request.user.is_staff:
        return redirect('Connexion_Admin')

    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword =  request.POST['repeatpasssword']
        genre = request.POST['genre']
        numTel = request.POST['numTel']
        adresse = request.POST['adresse']
        dateNaissance = request.POST['dateNaissance']
        specialite = request.POST['specialite']

        try:
            if password == repeatpassword:
                Medecin.objects.create(nom=nom,prenom=prenom,email=email,motdepasse=password,genre=genre,numTel=numTel,adresse=adresse,dateNaissance=dateNaissance,specialite=specialite)
                user = User.objects.create_user(first_name=nom,email=email,password=password,username=email)
                doc_group = Group.objects.get(name='Medecin')
                doc_group.user_set.add(user)
                user.save()
                error = "no"
            else:
                error = "yes"
        except Exception as e:
            error = "yes"
    d = {'error' : error}
    return render(request,'medecin/ajouterMedecin.html',d)

def voirMedecin(request):
    if not request.user.is_staff:
        return redirect('Connexion_Admin')
    doc = Medecin.objects.all()
    d = { 'doc' : doc }
    return render(request,'medecin/listeMedecin.html',d)

def supprimerMedecin(request,pk,email):  
    if not request.user.is_staff:
        return redirect('Connexion_Admin')  
    medecin=Medecin.objects.get(id=pk)
    if request.method=='POST':
        medecin.delete()
        users = User.objects.filter(username=email)
        users.delete()
        return redirect('listeMedecin')    
    context={'item':medecin}      
    return render(request, 'medecin/supprimerMedecin.html',context)    


def chercherMedecin(request): 
	erreur = ""
	query = request.GET["nom"]
	queryp = request.GET['prenom']
	nomMedecin=Medecin.objects.all().filter(nom__iexact=query)
	prenomMedecin=Medecin.objects.all().filter(prenom__iexact=queryp)
	if nomMedecin:
		if prenomMedecin:
			erreur = "no"
		else:
			erreur= "yes"	
	else:
		erreur = "yes"
	d = {'erreur':erreur}
	return render(request,'medecin/ajouterMedecin.html', d)		    

def modifier_medecin(request,pk):
    medecin=Medecin.objects.get(id=pk)
    formMedecin=MedecinForm(instance=medecin)

    if request.method=='POST':  #quand je click sur envoyer j'enregiste les modifs
	    formMedecin=MedecinForm(request.POST, instance=medecin)
	    if formMedecin.is_valid():
		     formMedecin.save()
		     return redirect('listeMedecin')
    context={'formMedecin':formMedecin}         
    return render(request, 'medecin/formMedecin.html',context) 


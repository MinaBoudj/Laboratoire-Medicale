from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from .forms import *

def AjouterReceptionniste(request):
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

        try:
            if password == repeatpassword:
                Receptionniste.objects.create(nom=nom,prenom=prenom,email=email,motdepasse=password,genre=genre,numTel=numTel,adresse=adresse,dateNaissance=dateNaissance)
                user = User.objects.create_user(first_name=nom,email=email,password=password,username=email)
                rec_group = Group.objects.get(name='Receptionniste')
                rec_group.user_set.add(user)
                user.save()
                error = "no"
            else:
                error = "yes"
        except Exception as e:
            error = "yes"
    d = {'error' : error}
    return render(request,'receptionniste/ajouterReceptionniste.html',d)

def voirReceptionniste(request):
    if not request.user.is_staff:
        return redirect('Connexion_Admin')
    rec = Receptionniste.objects.all()
    d = { 'rec' : rec }
    return render(request,'receptionniste/listeReceptionniste.html',d)


def supprimerReceptionniste(request,pk,email):
    if not request.user.is_staff:
        return redirect('Connexion_Admin')
    receptionniste=Receptionniste.objects.get(id=pk)
    if request.method=='POST':
        receptionniste.delete()
        users = User.objects.filter(username=email)
        users.delete()
        return redirect('listeReceptionniste')    
    context={'item':receptionniste}      
    return render(request, 'receptionniste/supprimerReceptionniste.html',context)    


def chercherReceptionniste(request): 
	erreur = ""
	query = request.GET["nom"]
	queryp = request.GET['prenom']
	nomRecep=Receptionniste.objects.all().filter(nom__iexact=query)
	prenomRecep=Receptionniste.objects.all().filter(prenom__iexact=queryp)
	if nomRecep:
		if prenomRecep:
			erreur = "no"
		else:
			erreur= "yes"	
	else:
		erreur = "yes"
	d = {'erreur':erreur}
	return render(request,'receptionniste/ajouterReceptionniste.html', d)		

def modifier_receptionniste(request,pk):
    receptionniste=Receptionniste.objects.get(id=pk)
    formReceptionniste=ReceptionnisteForm(instance=receptionniste)

    if request.method=='POST':  #quand je click sur envoyer j'enregiste les modifs
	    formReceptionniste=ReceptionnisteForm(request.POST, instance=receptionniste)
	    if formReceptionniste.is_valid():
		     formReceptionniste.save()
		     return redirect('listeReceptionniste')
    context={'formReceptionniste':formReceptionniste}         
    return render(request, 'receptionniste/formReceptionniste.html',context) 

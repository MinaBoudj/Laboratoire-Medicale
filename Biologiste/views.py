from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from .forms import *

def AjouterBiologiste(request):
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
                Biologiste.objects.create(nom=nom,prenom=prenom,email=email,motdepasse=password,genre=genre,numTel=numTel,adresse=adresse,dateNaissance=dateNaissance)
                user = User.objects.create_user(first_name=nom,email=email,password=password,username=email)
                bio_group = Group.objects.get(name='Biologiste')
                bio_group.user_set.add(user)
                user.save()
                error = "no"
            else:
                error = "yes"
        except Exception as e:
            error = "yes"
    d = {'error' : error}
    return render(request,'biologiste/ajouterBiologiste.html',d)

def voirBiologiste(request):
    if not request.user.is_staff:
        return redirect('Connexion_Admin')
    bio = Biologiste.objects.all()
    d = { 'bio' : bio }
    return render(request,'biologiste/listeBiologiste.html',d)


def supprimerBiologiste(request,pk,email):    
    biologiste=Biologiste.objects.get(id=pk)
    if request.method=='POST':
        biologiste.delete()
        users = User.objects.filter(username=email)
        users.delete()
        return redirect('listeBiologiste')    
    context={'item':biologiste}      
    return render(request, 'biologiste/supprimerBiologiste.html',context)    


def chercherBiologiste(request): 
	erreur = ""
	query = request.GET["nom"]
	queryp = request.GET['prenom']
	nomBiologiste=Biologiste.objects.all().filter(nom__iexact=query)
	prenomBiologiste=Biologiste.objects.all().filter(prenom__iexact=queryp)
	if nomBiologiste:
		if prenomBiologiste:
			erreur = "no"
		else:
			erreur= "yes"	
	else:
		erreur = "yes"
	d = {'erreur':erreur}
	return render(request,'biologiste/ajouterBiologiste.html', d)		



def modifier_biologiste(request,pk):
    biologiste=Biologiste.objects.get(id=pk)
    formBiologiste=BiologisteForm(instance=biologiste)

    if request.method=='POST':  #quand je click sur envoyer j'enregiste les modifs
	    formbiologiste=BiologisteForm(request.POST, instance=biologiste)
	    if formBiologiste.is_valid():
		     formBiologiste.save()
		     return redirect('listeBiologiste')
    context={'formBiologiste':formBiologiste}         
    return render(request, 'biologiste/formBiologiste.html',context) 

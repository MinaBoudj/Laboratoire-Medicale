from django.db import reset_queries
from django.http import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from Patient.models import *
from django.contrib.auth.models import User, Group
from datetime import date

# Create your views here.  


def detailDemande(request,pk):
    if not request.user.is_active:
        return redirect('PageAuthentification')
         
    demande=Demande.objects.get(id=pk)    
    liste_prelevement=Prelevement.objects.all().filter(id_demande=pk) 
    form=DemandeForm(instance=demande)	
    context={'demande':demande,'form':form , 'liste_prelevement':liste_prelevement}
    return render(request,'analyse/detaildemande.html',context)
                           


def ajouterDem(request,pk):
    erreurNb = ""
    error = ""
    patient=Patient.objects.get(id=pk)  
   
    form=DemandeForm() 
    if request.method=='POST':  #quand je click sur envoyer
        form=DemandeForm(request.POST)
        if form.is_valid():
            nomPatient = request.POST['nomPatient']
            prenomPatient = request.POST['prenomPatient']
            service = request.POST['service'] 
            nbr = request.POST['nb_prelevement']
            nature_prelevement1 = request.POST['nature_prelevement1']
            type_tube1 =request.POST['type_tube1']
            nature_prelevement2 = request.POST['nature_prelevement2']
            type_tube2 =request.POST['type_tube2']
            nature_prelevement3 = request.POST['nature_prelevement3']
            type_tube3 =request.POST['type_tube3']
            nature_prelevement4 = request.POST['nature_prelevement4']
            type_tube4 =request.POST['type_tube4']
                
            nomPa=Patient.objects.all().filter(nom__iexact=nomPatient)
            prenomPa=Patient.objects.all().filter(prenom__iexact=prenomPatient)            
            nomservice = Service.objects.all().filter(nomService__iexact=service)
            print(nbr)
               

            nb = 0
            if nomPa:
                    if prenomPa:  
                        if nomservice:
                            if nature_prelevement1 != "Aucun" and type_tube1 != "Aucun":
                                nb= nb+1
                                
                                #  insertion dans prelevement
                                if nature_prelevement2 !=  "Aucun" and type_tube2 != "Aucun":                                    
                                    # insertion dans prelevement
                                    if nature_prelevement3 !=  "Aucun" and type_tube3 != "Aucun":                      

                                        if nature_prelevement4 !=  "Aucun" and type_tube4 != "Aucun":
                                            if nbr == "4":
                                                erreurNb = "no"
                                                form.save()
                                                demande = Demande.objects.last()
                                                id_demande=demande.id
                                                Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement1,type_tube=type_tube1)  
                                                Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement2,type_tube=type_tube2)  
                                                Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement3,type_tube=type_tube3)
                                                Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement4,type_tube=type_tube4)
                                                return redirect('listeDemande')
                                            else:
                                                erreurNb = "yes"
                                                    
                                        else:
                                            if nbr == "3":
                                                erreurNb = "no"
                                                form.save()
                                                demande = Demande.objects.last()
                                                id_demande=demande.id
                                                Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement1,type_tube=type_tube1)  
                                                Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement2,type_tube=type_tube2)  
                                                Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement3,type_tube=type_tube3)
                                                                                                                                 
                                                return redirect('listeDemande')
                                            else:
                                                erreurNb = "yes"
                                                  
                                    else:
                                        if nbr == "2":
                                            form.save()
                                            demande = Demande.objects.last()
                                            id_demande=demande.id
                                            Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement1,type_tube=type_tube1)
                                            Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement2,type_tube=type_tube2)                                        
                                            return redirect('listeDemande')
                                        else:
                                            erreurNb = "yes"                                              

                                else:
                                    if nbr == "1":
                                        erreurNb = "no"
                                        error = "no"
                                        form.save()
                                        demande = Demande.objects.last()
                                        id_demande=demande.id
                                        Prelevement.objects.create(id_demande=id_demande,nature_prelevement=nature_prelevement1,type_tube=type_tube1)                                          
                                        return redirect('listeDemande')
                                    else:
                                        erreurNb = "yes"
                                           
                            else:
                                error = "yes"                                        
                                        
                                                            
                        else:
                            return redirect('ajouterDemande1')                        
                    else:
                     return redirect('ajouterDemande1')               
            else :
                return redirect('ajouterDemande1')                   
    context={'form':form, 'patient':patient , 'erreurNb':erreurNb, 'error':error}         
    return render(request, 'analyse/ajouterAnalyse.html',context)  



def voirDemande(request):
    if not request.user.is_active:
        return redirect('PageAuthentification')
    listeDemandeanalyse = Demande.objects.all()
    d = { 'listeDemandeanalyse' : listeDemandeanalyse }
    return render(request,'analyse/listeDemande.html',d)                 


def supprimerDemande(request,pk):    
    demande=Demande.objects.get(id=pk)
    if request.method=='POST':
        demande.delete()
        return redirect('listeDemande')    
    context={'item':demande}      
    return render(request, 'analyse/supprimerDemandeAnalyse.html',context)    


def modifierDemande(request,pk):
    demande=Demande.objects.get(id=pk)
    formDemande=DemandeForm(instance=demande)
    if request.method=='POST':  #quand je click sur envoyer j'enregiste les modifs
	    formDemande=DemandeForm(request.POST, instance=demande)
	    if formDemande.is_valid():            
             nomPatient = request.POST['nomPatient']
             prenomPatient = request.POST['prenomPatient']
             service = request.POST['service'] 
                   
             nomPa=Patient.objects.all().filter(nom__iexact=nomPatient)
             prenomPa=Patient.objects.all().filter(prenom__iexact=prenomPatient)
           
             nomservice = Service.objects.all().filter(nomService__iexact=service)   
             if nomPa:
                    if prenomPa:               
                                    if nomservice:
                                        formDemande.save()
                                        return redirect('listeDemande')
                                    else:
                                        return redirect('ajouterDemande1')                                  
                    else:
                     return redirect('ajouterDemande1')                  
             else :
                return redirect('ajouterDemande1')  
                                		     
    context={'formDemande':formDemande}         
    return render(request, 'analyse/formDemande.html',context)


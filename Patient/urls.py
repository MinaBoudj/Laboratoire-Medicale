from django.urls import path,include
from . import views

urlpatterns = [
    path('ajouter-Patient/',views.AjouterPatient,name='ajouterPatient'),
    path('dossierPatient/<str:pk>',views.dossierPatient,name='dossierPatient'),
    path('liste-patient/',views.voirPatient,name="listePatient"),
    path('modifier-patient/<str:pk>',views.modifier_patient,name="modifier_Patient"),
    path('patient/recherche',views.search,name="search"),
    path('supprimer_patient/<int:pk><str:email>',views.supprimerPatient,name="supprimerPatient"),
    
]
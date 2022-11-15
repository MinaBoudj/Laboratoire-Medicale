from django.urls import path,include
from . import views

urlpatterns = [
    path('ajouter-Medecin/',views.AjouterMedecin,name='ajouterMedecin'),
    path('liste-Medecin/',views.voirMedecin,name="listeMedecin"),
    path('supprimer-Medecin/<int:pk><str:email>',views.supprimerMedecin,name="supprimerMedecin"),
    path('medecin/recherche',views.chercherMedecin,name="chercherMedecin"),
    path('modifier-medecin/<str:pk>',views.modifier_medecin,name="modifierMedecin"),

]
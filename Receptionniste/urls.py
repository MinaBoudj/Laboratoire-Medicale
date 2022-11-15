from django.urls import path,include
from . import views

urlpatterns = [
    path('ajouter-Receptionniste/',views.AjouterReceptionniste,name='ajouterReceptionniste'),
    path('liste-Receptionniste/',views.voirReceptionniste,name="listeReceptionniste"),
    path('supprimer-Receptionniste/<int:pk><str:email>',views.supprimerReceptionniste,name="supprimerReceptionniste"),
    path('receptionniste/recherche',views.chercherReceptionniste,name="chercherReceptionniste"),
    path('modifier-reception/<str:pk>',views.modifier_receptionniste,name="modifierReceptionniste"),

    
]
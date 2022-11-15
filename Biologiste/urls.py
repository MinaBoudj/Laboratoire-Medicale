from django.urls import path,include
from . import views

urlpatterns = [
       path('ajouter-Biologiste/',views.AjouterBiologiste,name='ajouterBiologiste'),
       path('liste-Biologiste/',views.voirBiologiste,name="listeBiologiste"),
       path('supprimer-Biologiste/<int:pk><str:email>',views.supprimerBiologiste,name="supprimerBiologiste"),
       path('biologiste/recherche',views.chercherBiologiste,name="chercherBiologiste"),
       path('modifier-biologiste/<str:pk>',views.modifier_biologiste,name="modifierBiologiste"),

]
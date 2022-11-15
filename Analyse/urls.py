from django.urls import path,include
from . import views

urlpatterns = [
       path('listeDemande/',views.voirDemande,name='listeDemande'),  
       path('detailDemande/<str:pk>',views.detailDemande, name='detailDemande'),    
       path('modifierDemande/<str:pk>',views.modifierDemande, name="modifierDemande"),
       path('supprimerDemande/<str:pk>',views.supprimerDemande,name='supprimerDemande'),
       path('ajouter-DemandePatient/<str:pk>',views.ajouterDem,name='ajouterDemande1'),

]
from django.urls import path, include
from . import views

urlpatterns = [
       path('Statistique-Afficher', views.Statistique, name='Statistique-Afficher'),
       path('stat',views.Stat,name='stat'),
       path('ServiceStat', views.ServiceStat, name='ServiceStat'),
       path('BiochimieStat', views.BiochimieStat, name='BiochimieStat'),
       path('ParasitologieStat', views.ParasitologieStat, name='ParasitologieStat'),
       path('MicrobiologieStat', views.MicrobiologieStat, name='MicrobiologieStat'),
       path('HemobiologieStat', views.HemobiologieStat, name='HemobiologieStat'),
       path('PatientStat', views.StatistiquePatient, name='PatientStat'),

]

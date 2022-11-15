import django_filters
from .models import *

class Patientfilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = ['nom','prenom']
from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Service)
admin.site.register(DemandeAnalyse)
admin.site.register(Demande)
admin.site.register(Prelevement)
admin.site.register(AnalyseMicrobiologie)
admin.site.register(AnalyseParasitologie)
admin.site.register(AnalyseBiochimie)
admin.site.register(AnalyseHémobiologie)

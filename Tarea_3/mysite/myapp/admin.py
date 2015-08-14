from django.contrib import admin
from .models import Colegio, Ciencias,Historia, Lenguaje, Localidad, Matematicas,LenMat,PromedioGeneral, Ranking

# Register your models here.

class LocalidadInline(admin.TabularInline):
    model=Localidad
    extra=  0

class LenMatInline(admin.TabularInline):
    model=LenMat
    extra= 0

class LenguajeInline(admin.TabularInline):
    model=Lenguaje
    extra= 0
class MatematicasInline(admin.TabularInline):
    model=Matematicas
    extra= 0
class HistoriaInline(admin.TabularInline):
    model=Historia
    extra= 0
class CienciasInline(admin.TabularInline):
    model=Ciencias
    extra= 0
class PromedioGeneralInline(admin.TabularInline):
    model=PromedioGeneral
    extra= 0
class RankingInline(admin.TabularInline):
    model=Ranking
    extra= 0


       
    
class ColegioAdmin(admin.ModelAdmin):
    list_display = ('unidad_educativa' , 'rbd')
    inlines=(LocalidadInline, LenMatInline, LenguajeInline,MatematicasInline,  HistoriaInline,CienciasInline,PromedioGeneralInline, RankingInline,) 
    search_fields  =  [ 'unidad_educativa', 'rbd' ]

admin.site.register(Colegio, ColegioAdmin)




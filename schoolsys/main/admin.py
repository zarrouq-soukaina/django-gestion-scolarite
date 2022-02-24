from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Note ,User,Professeur,Etudiant,Filiere,PV,Niveau,Filiere

admin.site.site_header = "Gestion de scolarité"

@admin.register(Note)
class NoteAdmin(ImportExportModelAdmin):
    exclude = ('id', )   

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    exclude = ('id', ) 

@admin.register(Professeur)
class ProfesseurAdmin(ImportExportModelAdmin):
    exclude = ('id', )
    
@admin.register(Etudiant)
class EtudiantAdmin(ImportExportModelAdmin):
    exclude = ('id', )
    
@admin.register(Filiere)
class FiliereAdmin(ImportExportModelAdmin):
    exclude = ('id', )
    
@admin.register(Niveau)
class NiveauAdmin(ImportExportModelAdmin):
    exclude = ('id', )
    
@admin.register(PV)
class PV(ImportExportModelAdmin):
    exclude = ('id', )
    

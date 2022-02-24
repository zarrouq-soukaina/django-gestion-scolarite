import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class NoteFilter(django_filters.FilterSet):
	

	class Meta:
		model = Note
		fields = ('nom_mod','semestre','id_Etudiant')
		
class NoteEtudiantFilter(django_filters.FilterSet):
	

	class Meta:
		model = Note
		fields = ('nom_mod','semestre')
		
class ClasseFilter(django_filters.FilterSet):
	

	class Meta:
		model = Classe
		fields = ('nomC','annee_scolaire')
  
class FiliereFilter(django_filters.FilterSet):
	

	class Meta:
		model = Filiere
		fields = ('nom_F',)
  
class NiveauFilter(django_filters.FilterSet):
	

	class Meta:
		model = Niveau
		fields = ('niveau',)

class EtudiantFilter(django_filters.FilterSet):
	

	class Meta:
		model = Etudiant
		fields = ('user', 'niveau')
  
class ProfFilter(django_filters.FilterSet):
	

	class Meta:
		model = Professeur
		fields = ('user','statut')
  

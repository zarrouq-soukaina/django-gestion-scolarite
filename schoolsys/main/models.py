from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime
# Create your models here.


class  User(AbstractUser):
    prenom = models.CharField(max_length=20, null=True)
    nom = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=50, null=True)
    tel = models.CharField(max_length=20,null=True)
    is_etudiant = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_prof = models.BooleanField(default=False)
   
    
    def __str__(self):
        #return self.id_classe.nomC
        return f' {self.nom} {self.prenom}'
    
class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True,default='DEFAULT VALUE')
    statut= models.CharField(max_length=50, null=True)
    def __str__(self):
        #return self.id_classe.nomC
        return f' {self.user.nom} {self.user.prenom}'
        
class Niveau(models.Model):
   
    niveau = models.CharField(max_length=20)
    professeurs_n=models.ManyToManyField(Professeur)
    
    
    def __str__(self):
        #return self.id_classe.nomC
        return f'{self.niveau} '
    
    


   
class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True,default='DEFAULT VALUE')
    sexe_CHOICES = [('M','Male'),
                    ('F','Female'), 
                    ]
    CNE = models.IntegerField(null=True)
    sexe = models.CharField(max_length=20, null=True ,choices= sexe_CHOICES )
    naiss_date = models.DateField(max_length=30, null=True)
    nationalite = models.CharField(max_length=50, null=True)
    niveau= models.ForeignKey(Niveau, on_delete=models.CASCADE,null=True)
    def __str__(self):
        #return self.id_classe.nomC
        return f' {self.user.nom} {self.user.prenom} '
    
   
class Admin(models.Model):
    CHOICES =(
    ("Vacataire", "Vacataire"),
    ("Permanent", "Permanent"),
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, default='DEFAULT VALUE')
    status= models.CharField(max_length=60,null=True, choices = CHOICES)   


class Filiere(models.Model):
    nom_F = models.CharField(max_length=20,null=True)
    professeurs_f=models.ManyToManyField(Professeur)
    
    
    
    def __str__(self):
        return f' {self.nom_F} '
    


class Classe(models.Model):
    nomC = models.CharField(max_length=20,null=True) 
    annee_scolaire= models.CharField(max_length=20,null=True)
    id_Filiere= models.ForeignKey(Filiere, on_delete=models.CASCADE)
    id_Niveau= models.ForeignKey(Niveau, on_delete=models.CASCADE)
    nom_Prof= models.ForeignKey(Professeur, on_delete=models.CASCADE)
    etudiants=models.ManyToManyField(Etudiant)
    nmbre=models.IntegerField(default=0, blank=True, null=True)
    def __str__(self):
        return f'  {self.nomC} '
    



class PV(models.Model):
    fich_excel =models.FileField(null=True)
    id_classe= models.ForeignKey(Classe, on_delete=models.CASCADE)
    #admin=models.ManyToManyField(Admin)
    
   
    

class Note(models.Model):
    nom_mod = models.CharField(max_length=60)
    note= models.IntegerField()
    semestre_CHOICES = [('S1','Semestre 1'),
                    ('S2','Semestre 2'),
                    ]
    semestre = models.CharField(choices= semestre_CHOICES,max_length=20)
    id_PV= models.ForeignKey(PV, on_delete=models.CASCADE)
    id_Etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f' {self.nom_mod} {self.note} {self.semestre} {self.note} {self.id_Etudiant.user.nom}'

#    def __str__(self):
#        return self.nom_mod
#        return self.note
#        return self.semestre
#        return self.id_Etudiant 
    

class fichier (models.Model):
   etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE) 
   classe = models.ForeignKey(Classe, on_delete=models.CASCADE, default="default")
   anneScolaire = models.CharField(max_length=20, null=True )
   File_CHOICES = [('scolarite','scolarite'),
                    ('réussite','réussite'), 
                    ]
   type = models.CharField(max_length=20, null=True ,choices= File_CHOICES )
   dateganaration =  models.DateField(default=datetime.now)
   
   def __str__(self):
        return f' {self.dateganaration} {self.type} {self.classe.nomC} {self.etudiant.user.nom}'
    

    
    
    
    

   
   
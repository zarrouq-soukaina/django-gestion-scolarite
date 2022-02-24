from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django import forms
from django.db import transaction
from .models import *
from django.forms.widgets import NumberInput

class EtudiantSignUpForm(UserCreationForm):
    SEXE_CHOICES =(
    ("F", "Female"),
    ("M", "Male"),
    )
    nom = forms.CharField(required=False)
    prenom = forms.CharField(required=False)
    email=forms.EmailField(required=False)
    tel=forms.IntegerField(required=False)
    CNE=forms.IntegerField(required=False)
    #sexe = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = SEXE_CHOICES,required=False)
    sexe = forms.ChoiceField(widget=forms.RadioSelect,choices = SEXE_CHOICES,required=False)
    #naiss_date =forms.DateField(required=False,widget=forms.SelectDateWidget)
    naiss_date  = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    nationalite=forms.CharField(required=False)
    Niveau = forms.ModelChoiceField(queryset=Niveau.objects.all(),required=False)
    #Filiere = forms.ModelChoiceField(queryset=Filiere.objects.all(),required=False)
    #Classe = forms.ModelChoiceField(queryset=Classe.objects.all(),required=False)
    #image = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_etudiant = True
        user.nom = self.cleaned_data.get('nom')
        user.prenom = self.cleaned_data.get('prenom')
        user.email=self.cleaned_data.get('email')
        user.tel=self.cleaned_data.get('tel')
        #user.profile_pic=self.cleaned_data.get('image')

        #user.is_active = False
        user.save()
        etudiant = Etudiant.objects.create(user=user)
        etudiant.CNE=self.cleaned_data.get('CNE')
        etudiant.naiss_date=self.cleaned_data.get('naiss_date')
        #etudiant.naiss_date=self.cleaned_data.get('Date_de_naissance')
        etudiant.nationalite=self.cleaned_data.get('nationalite')
        etudiant.sexe=self.cleaned_data.get('sexe')
        etudiant.niveau=self.cleaned_data.get('Niveau')
        #etudiant.Filiere=self.cleaned_data.get('Filiere')
        etudiant.save()
        return user

class ProfesseurSignUpForm(UserCreationForm):
    nom = forms.CharField(required=False)
    prenom = forms.CharField(required=False)
    email=forms.EmailField(required=False)
    tel=forms.IntegerField(required=False)
    CHOICES =(
    ("Vacataire", "Vacataire"),
    ("Permanent", "Permanent"),
    )
    statut = forms.ChoiceField(widget=forms.RadioSelect,choices = CHOICES,required=False)
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_prof= True
        user.nom = self.cleaned_data.get('nom')
        user.prenom = self.cleaned_data.get('prenom')
        user.email=self.cleaned_data.get('email')
        user.tel=self.cleaned_data.get('tel')
        user.save()
        professeur = Professeur.objects.create(user=user)
        professeur.statut=self.cleaned_data.get('statut')
        professeur.save()
        return user

class AdminSignUpForm(UserCreationForm):
    nom = forms.CharField(required=False)
    prenom = forms.CharField(required=False)
    email=forms.EmailField(required=False)
    CHOICES =(
    ("Vacataire", "Vacataire"),
    ("Permanent", "Permanent"),
    )
    statut = forms.ChoiceField(widget=forms.RadioSelect,choices = CHOICES,required=False)
    
    class Meta(UserCreationForm.Meta):
        model = User
     
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.nom = self.cleaned_data.get('nom')
        user.prenom = self.cleaned_data.get('prenom')
        user.email=self.cleaned_data.get('email')
        user.save()
        admin = Admin.objects.create(user=user)
        admin.statut=self.cleaned_data.get('statut')
        admin.save()
        return user
 


        
class AdminForm(forms.ModelForm):
    
    
   class Meta:
        model = User
        fields = '__all__'    
        exclude = {'password','last_login','is_superuser','username','first_name','last_name','is_staff','is_active','date_joined','is_etudiant','is_admin','is_prof','gourp_id','permission_id'}
         
class ProfesseurForm(forms.ModelForm):
   class Meta:
       model = User
       fields = '__all__' 
       exclude = {'password','last_login','is_staff','is_admin','date_joined','groups','is_active', 'is_superuser','codename','profile_pic','username','first_name','last_name'}
         
class EtudiantForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' 
        exclude = {'password','last_login','is_staff','is_admin','date_joined','groups','is_active', 'is_superuser','codename','profile_pic','username','first_name','last_name'}
    
class NiveauForm(forms.ModelForm):
    professeurs_n = forms.ModelMultipleChoiceField(queryset=Professeur.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Niveau
        
        fields = '__all__'
        
        
        
        
class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = '__all__'
       
        
class ClasseForm(forms.ModelForm):
    etudiants = forms.ModelMultipleChoiceField(queryset=Etudiant.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Classe
        fields = '__all__'
        exclude = {'nmbre'}
        
        #products = forms.MultipleChoiceField(queryset=Product.objects.all(), label='Manager', required=True)
        
class PVForm(forms.ModelForm):
    class Meta:
        model = PV
        fields = '__all__'
       
        
        
class FiliereForm(forms.ModelForm):
    professeurs_f = forms.ModelMultipleChoiceField(queryset=Professeur.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Filiere 
        fields = '__all__'
        #exclude = {'dateganaration'}
        
class FileForm(forms.ModelForm):
    class Meta:
        model = fichier
        fields = '__all__'
        exclude = {'dateganaration'}
        
        
class AddForm(forms.ModelForm):
    etudiants = forms.ModelMultipleChoiceField(queryset=Etudiant.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Classe
        fields = ('etudiants',)
        
class AddprofForm(forms.ModelForm):
    professeurs_f = forms.ModelMultipleChoiceField(queryset=Professeur.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Filiere 
        fields = ('professeurs_f',)
        
class AddprofsForm(forms.ModelForm):
    professeurs_n = forms.ModelMultipleChoiceField(queryset=Professeur.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Niveau
        fields = ('professeurs_n',)
    

       
class PasswordChangeingForm(PasswordChangeForm):
    old_password = forms.PasswordInput
    new_password1 = forms.PasswordInput
    new_password2 = forms.PasswordInput
    
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')
    
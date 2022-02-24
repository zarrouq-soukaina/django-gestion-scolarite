from django.contrib.auth import login, logout,authenticate
from django.http.response import HttpResponseBadRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from reportlab.lib import pagesizes

from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.core.mail import EmailMessage
from django.views.generic import View

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .tokens import account_activation_token
from django.core.mail import EmailMessage 
from django.conf import settings


from django.contrib.auth.tokens import PasswordResetTokenGenerator


from django.contrib import messages

from .form import *

from django.shortcuts import render
from django.http import HttpResponse
from .resources import NoteResource
from tablib import Dataset

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .filters import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import  PasswordChangeView
from django.urls import reverse_lazy

def register(request):
    return render(request, '../templates/registration/register.html')

class PasswordsChangeView(PasswordChangeView):
    from_class =PasswordChangeingForm 
    success_url = reverse_lazy('password_succes')
    
def password_succes(request):
    return render(request, 'registration/password_succes.html' , {})
class generate_pdr(CreateView):
    model = fichier
    form_class= FileForm
    template_name = '../templates/fichier/generate.html'
    def form_valid(self, form):
        
        fiche = form.save()
        et = fiche.etudiant
        t = fiche.type
        infos = fichier.objects.get(type=fiche.type,classe = fiche.classe,etudiant=fiche.etudiant,anneScolaire=fiche.anneScolaire )
        if t=="scolarite":
            
             # create Bytestream buffer
            buf = io.BytesIO()
            #create a canvas
            c = canvas.Canvas(buf, pagesize= letter,bottomup = 0)
            #create text object
            textob = c.beginText()
            textob.setTextOrigin(inch, inch)
            
            textob.setFont("Helvetica", 14)
                #add some lines of text
            lines = [
		    
	               ]
            lines.append("attestation de scolarité:")
            lines.append("Le directeur de l'Institut National de Statistique et d'Economie appliquée de Rabat  ")
            lines.append("certifie que l'étudiant(e)  ")
           
            lines.append(infos.etudiant.user.nom)
            
            lines.append(infos.etudiant.user.prenom)
            lines.append("est inscrit(e) à l'institut durant l'année scolaire:")
            
            lines.append(infos.anneScolaire)
            
            lines.append("En foi de quoi la présente attestation lui a été délivrée pour servir et valoir")
            lines.append("ce que de droit.")
            
                #Loop  
                
            for line in lines:
                textob.textLine(line)
        
                  #Finish Up
            c.drawText(textob)
            c.showPage()
            c.save()
            buf.seek(0)
            return FileResponse(buf, as_attachment=True, filename="scolarité.pdf")
        
        else:
            if t =="réussite":
                 # create Bytestream buffer
                buf = io.BytesIO()
                #create a canvas
                c = canvas.Canvas(buf, pagesize= letter,bottomup = 0)
                #create text object
                textob = c.beginText()
                textob.setTextOrigin(inch, inch)
            
                textob.setFont("Helvetica", 14)
                #add some lines of text
                lines = [
		    
	               ]
                lines.append("attestation de réussite:")
                lines.append("type:")
                lines.append(infos.type)
                lines.append("année scolaire:")
                lines.append(infos.anneScolaire)
                lines.append("nom étudiant:")
                lines.append(infos.etudiant.user.nom)
                lines.append("prénom étudiant:")
                lines.append(infos.etudiant.user.prenom)
                
                #Loop  
                
                
                for line in lines:
                   textob.textLine(line)
        
                  #Finish Up
                c.drawText(textob)
                c.showPage()
                c.save()
                buf.seek(0)
                return FileResponse(buf, as_attachment=True, filename="réussite.pdf")
        return redirect('/')
                
            
        
       
        

class etudiant_register(CreateView):
    model = User
    form_class = EtudiantSignUpForm
    template_name = '../templates/registration/etudiant_register.html'
    
    

    def form_valid(self, form):
        user = form.save()
        email=user.email
       
        
        current_site = get_current_site(self.request)
        email_subject = 'Active your Account'
        message = render_to_string('registration/activate.html',
                                   {
                                       'user': user,
                                       'domain': current_site.domain,
                                       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                       'token': account_activation_token.make_token(user)
                                   }
                                   )
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                        email_subject, message,  settings.EMAIL_HOST_USER,to=[to_email]
            )
        email.send()
           

    

        login(self.request, user)
        return redirect('/')

class professeur_register(CreateView):
    model = User
    form_class = ProfesseurSignUpForm
    template_name = '../templates/registration/professeur_register.html'

    def form_valid(self, form):
        user = form.save()
        email=user.email
       
        
        current_site = get_current_site(self.request)
        email_subject = 'Active your Account'
        message = render_to_string('registration/activate.html',
                                   {
                                       'user': user,
                                       'domain': current_site.domain,
                                       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                       'token': account_activation_token.make_token(user)
                                   }
                                   )
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                        email_subject, message,  settings.EMAIL_HOST_USER,to=[to_email]
            )
        email.send()
           

        login(self.request, user)
        return redirect('/')

class admin_register(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = '../templates/registration/admin_register.html'

    def form_valid(self, form):
        user = form.save()
        email=user.email
       
        
        current_site = get_current_site(self.request)
        email_subject = 'Active your Account'
        message = render_to_string('registration/activate.html',
                                   {
                                       'user': user,
                                       'domain': current_site.domain,
                                       'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                       'token': account_activation_token.make_token(user)
                                   }
                                   )
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                        email_subject, message,  settings.EMAIL_HOST_USER,to=[to_email]
            )
        email.send()
           

        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if user.is_active and user.is_etudiant:
                    return redirect('/etudiant') #Go to student home
                elif user.is_active and user.is_admin:
                    return redirect('adminScolarité') #Go to admin home
                elif user.is_active and user.is_prof:
                    return redirect('prof') #Go to teacher home

            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/registration/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 'account activated successfully')
            return redirect('login')
        return render(request, '../templates/registration/activate_failed.html', status=401)
    
def homeAdmin(request): 
     classes = Classe.objects.all()
     filieres = Filiere.objects.all()
     niveaux = Niveau.objects.all()
     profs = Professeur.objects.all()
     etuds = Etudiant.objects.all()
     pvs= PV.objects.all()
     total_filieres = filieres.count()
     total_classes = classes.count()
     total_niveaux = niveaux.count()
     total_prof = profs.count()
     total_etud= etuds.count()
     total_pv=pvs.count()
     
     
     context = {'classes':classes, 'filieres':filieres,
	'total_classes':total_classes,'total_filieres':total_filieres,
	'niveaux':niveaux, 'total_niveaux':total_niveaux, 'profs': profs, 'etuds': etuds, 'total_prof':total_prof, 'total_etud': total_etud, 'pvs':pvs, 'total_pv':total_pv}
     
     return render(request, '../templates/registration/admin_home.html', context)

def homeEtudiant(request):
    if request.user.is_authenticated:
        etu = Etudiant.objects.get(user=request.user)
        context = {'etu':etu}
    
    return render(request, '../templates/registration/etudiant_home.html', context)

def homeEProf(request):
     if request.user.is_authenticated:
        prof = Professeur.objects.get(user=request.user)
        context = {'prof':prof}
        return render(request, '../templates/registration/prof_home.html', context) 

 
  
        


#Fonctions CRUD de la classe professeur
def indexP(request):
    prof = Professeur.objects.all()
    myFilter = ProfFilter(request.GET, queryset=prof)
    prof = myFilter.qs
    context = {'prof':prof,'myFilter':myFilter} 
   
    return render(request, 'professeur/indexP.html',context)

def createP(request):
	form = ProfesseurForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ProfesseurForm(request.POST)
		if form.is_valid():
      
            #form.is_admin= True
            
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'professeur/createP.html', context)

def updateP(request, pk):
	pr = User.objects.filter(id= pk)
	form = ProfesseurForm(instance=pr)
	if request.method == 'POST':
		form = ProfesseurForm(request.POST, instance=pr)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'professeur/createP.html', context)

def deleteP(request, pk):
	pr = User.objects.get(id= pk)
	if request.method == "POST":
		pr.delete()
		return redirect('indexP')

	context = {'item':pr}
	return render(request, 'professeur/deleteP.html', context)





#celle ci qui doit fonctionner seulement (idem pour admin et etudiant)
def viewP(request,pk):
   prof = Professeur.objects.get(user = pk)
   return render(request, 'professeur/viewP.html',{'prof':prof})

#Fonctions CRUD de la classe admin


def createA(request):
	form = AdminForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = AdminForm(request.POST)
		if form.is_valid():
      
            #form.is_admin= True
            
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'admin/createA.html', context)

def updateA(request, pk):

	ad = User.objects.filter( is_admin= True)
	form = AdminForm(instance=ad)

	if request.method == 'POST':
		form = AdminForm(request.POST, instance=ad)
		if form.is_valid():
			form.save()
            
			return redirect('/')
    
	context = {'form':form}
	return render(request, 'admin/createA.html', context)


def deleteA(request, pk):
	ad = User.objects.get(is_admin= True)
	if request.method == "POST":
		ad.delete()
		return redirect('/')

	context = {'item':ad}
	return render(request, 'admin/deleteA.html', context)





def viewA(request,pk):
    var = User.objects.get(id = pk)
    return render(request, 'admin/viewA.html',{'var':var})


#Fonctions CRUD de la classe etudiant
def indexE(request):
    
    etu = Etudiant.objects.all()
    myFilter = EtudiantFilter(request.GET, queryset=etu)
    etu = myFilter.qs
    context = {'etu':etu,'myFilter':myFilter} 
    
    return render(request, 'classe/indexE.html',context)

def createE(request):
	form = EtudiantForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = EtudiantForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'etudiant/createE.html', context)
def updateN(request, pk):

	niv = Niveau.objects.get(id=pk)
	form = NiveauForm(instance=niv)

	if request.method == 'POST':
		form = NiveauForm(request.POST, instance=niv)
		if form.is_valid():
			form.save()
			return redirect('adminScolarité')

	context = {'form':form}
	return render(request, 'niveau/createN.html', context)


def updateE(request, pk):

	etu = Etudiant.objects.get(user=pk)
	form = EtudiantForm(instance=etu)

	if request.method == 'POST':
		form = EtudiantForm(request.POST, instance=etu)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'etudiant/createE.html', context)

def deleteE(request, pk):
	etu = User.objects.get(id=pk)
	if request.method == "POST":
		etu.delete()
		return redirect('indexE')

	context = {'item':etu}
	return render(request, 'etudiant/deleteE.html', context)




def viewE(request,pk):
    etu = Etudiant.objects.get(user = pk)
    return render(request, 'etudiant/viewE.html',{'etu':etu})



#Fonctions CRUD de la classe filière

#def addEtudi(request,pk):

def proff(request,pk):
    
    filiere = Filiere.objects.get(id=pk)
    
    profs = filiere.professeurs_f.all()
    myFilter = ProfFilter(request.GET, queryset=profs)
    profs = myFilter.qs
    context = {'profs':profs,'myFilter':myFilter} 
    return render(request, 'filiere/indexProf.html',context)

def indexF(request):
    var= Filiere.objects.all()
    myFilter = FiliereFilter(request.GET, queryset=var)
    var = myFilter.qs
    context = {'var':var,'myFilter':myFilter} 
    
    return render(request, 'filiere/indexF.html',context)
  
  
def createF(request):
    form = FiliereForm()
    if request.method == 'POST':
        form = FiliereForm(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.save()
            professeurs_f = request.POST.getlist('professeurs_f')
            for professeur_f in professeurs_f:
                if Professeur.objects.all().exists():
                    professeur_f = Professeur.objects.get(user=professeur_f)
                    data.professeurs_f.add(professeur_f)
        return redirect('adminScolarité')
    context = {'form':form}
    return render(request, 'filiere/createF.html', context)



def updateF(request, pk):

	fi = Filiere.objects.get(id=pk)
	form = FiliereForm(instance=niv)

	if request.method == 'POST':
		form = FiliereForm(request.POST, instance=fi)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'filiere/createF.html', context)

def deleteF(request, pk):
	fi = Filiere.objects.get(id=pk)
	if request.method == "POST":
		fi.delete()
		return redirect('/')

	context = {'item':fi}
	return render(request, 'filiere/deleteF.html', context)


def viewF(request,pk):
    fi = Filiere.objects.get(id = pk)
    return render(request, 'filiere/viewF.html',{'fi':fi})

def addprofs(request, pk): 
    form = AddprofForm()
    if request.method == 'POST':
        form = AddprofForm(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.id=Filiere.objects.get(id=pk).id
            data.nom_F=Filiere.objects.get(id=pk).nom_F
            
            
            fil = Filiere.objects.get(id=pk)
            professeurs_f = request.POST.getlist('professeurs_f')
            for professeur_f in professeurs_f:
                if Professeur.objects.all().exists():
                    professeur_f = Professeur.objects.get(user=professeur_f)
                    fil.professeurs_f.add(professeur_f)
            
            data.save()
            
        return redirect('indexF')
    context = {'form':form}
    return render(request, 'filiere/addprofs.html', context)

def addprof(request, pk): 
    form = AddprofsForm()
    if request.method == 'POST':
        form = AddprofsForm(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.id=Niveau.objects.get(id=pk).id
            data.niveau=Niveau.objects.get(id=pk).niveau
            
            
            niveau = Niveau.objects.get(id=pk)
            professeurs_n = request.POST.getlist('professeurs_n')
            for professeur_n in professeurs_n:
                if Professeur.objects.all().exists():
                    professeur_n = Professeur.objects.get(user=professeur_n)
                    niveau.professeurs_n.add(professeur_n)
            
            data.save()
            
        return redirect('indexN')
    context = {'form':form}
    return render(request, 'niveau/addprofs.html', context)


#Fonctions CRUD de la classe niveau

def indexN(request):
    var= Niveau.objects.all()
    
    myFilter = NiveauFilter(request.GET, queryset=var)
    var = myFilter.qs
    context = {'var':var,'myFilter':myFilter} 

   
    return render(request, 'niveau/indexN.html',context)

def createN(request):
    form = NiveauForm()
    if request.method == 'POST':
        form = NiveauForm(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.save()
            professeurs_n = request.POST.getlist('professeurs_n')
            for professeur_n in professeurs_n:
                if Professeur.objects.all().exists():
                    professeur_n = Professeur.objects.get(user=professeur_n)
                    data.professeurs_n.add(professeur_n)
        return redirect('/')
    context = {'form':form}
    return render(request, 'niveau/createN.html', context)

def ProfN(request,pk):
    
    niveau = Niveau.objects.get(id=pk)
    
    profs = niveau.professeurs_n.all()
    myFilter = ProfFilter(request.GET, queryset=profs)
    profs = myFilter.qs
    context = {'profs':profs,'myFilter':myFilter} 
    
    return render(request, 'niveau/indexP.html',context)


def updateN(request, pk):

	niv = Niveau.objects.get(id=pk)
	form = NiveauForm(instance=niv)

	if request.method == 'POST':
		form = NiveauForm(request.POST, instance=niv)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'niveau/createN.html', context)

def deleteN(request, pk):
	niv = Niveau.objects.get(id=pk)
	if request.method == "POST":
		niv.delete()
		return redirect('/')

	context = {'item':niv}
	return render(request, 'niveau/deleteN.html', context)

def viewN(request,pk):
   niv = Niveau.objects.get(id = pk)
   return render(request, 'niveau/viewN.html',{'niv':niv})

#Fonctions CRUD de la classe 'classe'
def createC(request):
    form = ClasseForm()
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.save()
            etudiants = request.POST.getlist('etudiants')
            for etudiant in etudiants:
                if Etudiant.objects.all().exists():
                    etudiant = Etudiant.objects.get(user=etudiant)
                    data.etudiants.add(etudiant)
        return redirect('adminScolarité')
    context = {'form':form}
    return render(request, 'classe/createC.html', context)
	#return render(request, 'classe/createC.html', context)

def addEtudiants(request, pk): 
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            data= form.save(commit=False)
            data.id=Classe.objects.get(id=pk).id
            data.id_Filiere=Classe.objects.get(id=pk).id_Filiere
            data.id_Niveau=Classe.objects.get(id=pk).id_Niveau
            data.nom_Prof=Classe.objects.get(id=pk).nom_Prof
            data.nomC=Classe.objects.get(id=pk).nomC
            
            classe = Classe.objects.get(id=pk)
            etudiants = request.POST.getlist('etudiants')
            for etudiant in etudiants:
                if Etudiant.objects.all().exists():
                    etudiant = Etudiant.objects.get(user=etudiant)
                    classe.etudiants.add(etudiant)
            
            data.save()
            
        return redirect('indexC')
    context = {'form':form}
    return render(request, 'classe/addEtudiants.html', context)

    
                    
def indexC(request):
    

    cl = Classe.objects.all() 
    myFilter = ClasseFilter(request.GET, queryset=cl)
    cl = myFilter.qs
    
    context = {'cl':cl,'myFilter':myFilter} 
    return render(request, 'classe/indexC.html', context)
 
def pvC(request,pk):
    
    pvs = PV.objects.filter(id_classe=pk)

    return render(request, 'classe/indexPV.html',{'pvs':pvs})
#la liste des étudiant par classe

def EtudiantC(request,pk):
    
    classes = Classe.objects.get(id=pk)
    
    etu = classes.etudiants.all() 
    myFilter = EtudiantFilter(request.GET, queryset=etu)
    etu = myFilter.qs
    context = {'etu':etu,'myFilter':myFilter} 
   
        


    return render(request, 'classe/indexE.html',context)
           
            
            
        
        
        
            
        
        
       


def updateC(request, pk):

	cl = Classe.objects.get(id=pk)
	form = ClasseForm(instance=cl)

	if request.method == 'POST':
		form = ClasseForm(request.POST, instance=cl)
		if form.is_valid():
			form.save()
			return redirect('indexC')

	context = {'form':form}
	return render(request, 'classe/updateC.html', context)

def deleteC(request, pk):
	cl = Classe.objects.get(id=pk)
	if request.method == "POST":
		cl.delete()
		return redirect('/')

	context = {'item':cl}
	return render(request, 'classe/deleteC.html', context)

def viewC(request,pk):
   cl = Classe.objects.get(id = pk)
   return render(request, 'classe/viewC.html',{'cl':cl})
def pvC(request,pk):
    
    pvs = PV.objects.filter(id_classe=pk)

    return render(request, 'classe/indexPV.html',{'pvs':pvs})



    



#Fonctions CRUD de la classe 'Note'
def indexM(request): 
    var= Note.objects.all()
    myFilter = NoteFilter(request.GET, queryset=var)
    var = myFilter.qs
    context = {'var':var,'myFilter':myFilter} 

    return render(request, 'note/indexM.html', context)

def createM(request):
	form = NoteForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = NoteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'note/createM.html', context)

def updateM(request, pk):

	no = Note.objects.get(id=pk)
	form = NoteForm(instance=niv)

	if request.method == 'POST':
		form = NoteForm(request.POST, instance=no)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'note/createM.html', context)

def deleteM(request, pk):
	no = Note.objects.get(id=pk)
	if request.method == "POST":
		no.delete()
		return redirect('/')

	context = {'item':no}
	return render(request, 'note/deleteM.html', context)


def viewM(request,pk):
   no = Note.objects.get(id = pk)
   return render(request, 'note/viewM.html',{'no':no})

#Fonctions CRUD de la classe PV

def createPV(request):
	form = PVForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = PVForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'pv/createPV.html', context)

def updatePV(request, pk):

	pv = PV.objects.get(id=pk)
	form = PVForm(instance=pv)

	if request.method == 'POST':
		form = PVForm(request.POST, instance=pv)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'pv/createPV.html', context)

def deletePV(request, pk):
	pv = PV.objects.get(id=pk)
	if request.method == "POST":
		pv.delete()
		return redirect('indexP')

	context = {'item':pv}
	return render(request, 'pv/deletePV.html', context)

def viewPV(request,pk):
   pv = PV.objects.get(id = pk)
   return render(request, 'pv/viewPV.html',{'pv':pv})



def export(request):
    Note_resource = NoteResource()
    dataset = Note_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Notes.xls"'
    return response

def simple_upload(request):
    if request.method == 'POST':
        Note_resource = NoteResource()
        dataset = Dataset()
        new_Notes = request.FILES['myfile']

        imported_data = dataset.load(new_Notes.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Note(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
        		 data[4]
        		)
        	value.save()       
        
        #result = Note_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    Note_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'pv/createPV.html')

def noteEtudiant(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Etudiant, user=request.user)
        notes = Note.objects.filter(id_Etudiant=user)
        myFilter = NoteEtudiantFilter(request.GET, queryset=notes)
        notes = myFilter.qs
        context = {'notes':notes,'myFilter':myFilter} 
        return render(request, 'etudiant/note.html', context)
    
def classEtudiant(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Etudiant, user=request.user)
        classes = Classe.objects.filter(etudiants=user)
        myFilter = ClasseFilter(request.GET, queryset=classes)
        classes = myFilter.qs
        context = {'classes':classes,'myFilter':myFilter} 
        return render(request, 'etudiant/classe.html', context)
    
def classProf(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Professeur, user=request.user)
        classes = Classe.objects.filter(nom_Prof=user)
        myFilter = ClasseFilter(request.GET, queryset=classes)
        classes = myFilter.qs
        context = {'classes':classes,'myFilter':myFilter} 
        return render(request, 'professeur/classe.html', context)
    

    
def search_noteEt(request):
    if 'nom_mod' in request.GET:
        nom_mod = request.GET['nom_mod']
        if nom_mod:
            notes = Note.filter(nom_mod=nom_mod)
    context = {

        'notes': notes,

    }
    return render(request, 'etudiant/note.html', context)




def search_etudiant(request):
    if 'nom' in request.GET:
        nom = request.GET['nom']
        if nom:
            etudiant = Etudiant.filter(nom=user.nom)
    context = {

        'notes': notes,

    }
    return render(request, 'etudiant/note.html', context)









def simple_upload(request):
    if request.method == 'POST':
        Note_resource = NoteResource()
        dataset = Dataset()
        new_Notes = request.FILES['myfile']

        imported_data = dataset.load(new_Notes.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Note(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
        		 data[4]
        		)
        	value.save()       
        


#abscence
class import_data(forms.Form):
    fich_excel = forms.FileField()
def abscence (request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            request.FILES["fich_excel"].save_to_database(
                models=Abscence,
                mapdicts=
                    ["nom_mod", "classe", "etudiant","date"] )
            return redirect('/')
        else:
            return HttpResponseBadRequest()
    else:
        return render(request, 'fichier/abscence.html', {})

  
  


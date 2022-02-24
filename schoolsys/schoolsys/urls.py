from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from main.views import *
from  django.contrib.auth.views import PasswordChangeView 


urlpatterns = [
    path('main/', include('main.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('etudiant/',homeEtudiant, name='etudiant'),
    path('prof/',homeEProf, name='prof'),
    path('adminScolarité/',homeAdmin, name='adminScolarité'),
    
    path('etudiant/change_password/', PasswordsChangeView.as_view(template_name="registration/password_reset_form.html"), name="change_password"),
    path('adminScolarité/change_password/', PasswordsChangeView.as_view(template_name="registration/password_reset_form.html"), name="change_password"),
    path('prof/change_password/', PasswordsChangeView.as_view(template_name="registration/password_reset_form.html"), name="change_password"),

    path('password_succes',password_succes, name='password_succes'),
    
    path('adminScolarité/indexE',indexE,name='indexE'),
    path('adminScolarité/indexP',indexP,name='indexP'),
    path('adminScolarité/indexC',indexC,name='indexC'),
    path('adminScolarité/indexN',indexN,name='indexN'),
    path('adminScolarité/indexF',indexF,name='indexF'),
    path('adminScolarité/indexM',indexM,name='indexM'),
    path('adminScolarité/createF',createF,name='createF'),
    path('adminScolarité/createC',createC,name='createC'),
    path('adminScolarité/createN',createN,name='createN'),
    path('adminScolarité/createM',createM,name='createM'),
    path('adminScolarité/createE',createE,name='createE'),
    path('adminScolarité/createP',createP,name='createP'),
    path('adminScolarité/generate_pdr/',generate_pdr.as_view(), name='generate_pdr'),

    
    #CRUD
    path('createP/',createP),
    path('listP/',indexP),
    #path('viewP/<int:pk>',viewP,name='viewP'),
    path('listP/viewP/<int:pk>',viewP,name='viewP'),
    path('deleteP/<int:pk>',deleteP,name='deleteP'),
    path('updateP/<int:pk>',updateP, name='updateP'),
    path('prof/classProf/',classProf, name='classProf'),

    
    path('createA/',createA),
    #path('listA/',indexA),
    path('viewA/<int:pk>',viewA,name='viewA'),
    path('deleteA/<int:pk>',deleteA,name='deleteA'),
    path('updateA/<int:pk>',updateA, name='updateA'),

    
    path('createE/',createE),
    path('listE/',indexE),
    path('listE/viewE/<int:pk>',viewE,name='viewE'),
    path('deleteE/<int:pk>',deleteE,name='deleteE'),
    path('updateE/<int:pk>',updateE, name='updateE'),
    path('etudiant/classEtudiant/',classEtudiant, name='classEtudiant'),
    path('etudiant/noteEtudiant',noteEtudiant,name='noteEtudiant'),
    
    path('createF/',createF),
    path('listF/',indexF),
    path('viewF/<int:pk>',viewF,name='viewF'),
    path('deleteF/<int:pk>',deleteF,name='deleteF'),
    path('updateF/<int:pk>',updateF, name='updateF'),
    path('indexF/',indexF, name='indexF'), 
    path('proff/<int:pk>',proff, name='proff'),
    path('addprofs/<int:pk>',addprofs, name='addprofs'),

    
    path('createN/',createN),
    path('listN/',indexN),
    path('viewN/<int:pk>',viewN,name='viewN'),
    path('deleteN/<int:pk>',deleteN,name='deleteN'),
    path('updateN/<int:pk>',updateN, name='updateN'),
    path('ProfN/<int:pk>',ProfN, name='ProfN'),
    path('addprof/<int:pk>',addprof, name='addprof'),
    
    path('createC/',createC),
    path('listC/',indexC),
    path('viewC/<int:pk>',viewC,name='viewC'),
    path('deleteC/<int:pk>',deleteC,name='deleteC'),
    path('updateC/<int:pk>',updateC, name='updateC'),
    path('pvC/<int:pk>',pvC, name='pvC'),
    path('EtudiantC/<int:pk>',EtudiantC, name='EtudiantC'),
    path('addEtudiants/<int:pk>',addEtudiants, name='addEtudiants'),
    
    path('createM/',createM),
    path('listM/',indexM),
    path('viewM/<int:pk>',viewM,name='viewM'),
    path('deleteM/<int:pk>',deleteM,name='deleteM'),
    path('updateM/<int:pk>',updateM, name='updateM'),

    
    path('createPV/',createPV,name="createPV"),
    #path('listPV/',indexPV),
    path('viewPV/<int:pk>',viewPV,name='viewPV'),
    path('deletePV/<int:pk>',deletePV,name='deletePV'),
    path('updatePV/<int:pk>',updatePV, name='updatePV'),
    
    #path('Import_csv/', import_csv,name="Import_csv"), 
    
    
    

    
     path('etudiant/reset',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
     name="password_reset_confirm"),
    
    #abscence 
    path('import_data',import_data,name='import_data'),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.contrib.auth import views as auth_views
from  django.contrib.auth.views import PasswordChangeView 
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('etudiant_register/',views.etudiant_register.as_view(), name='etudiant_register'),
     path('admin_register/',views.admin_register.as_view(), name='admin_register'),
     path('professeur_register/',views.professeur_register.as_view(), name='professeur_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'), 
     path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), 
        name="password_reset_complete"),
    #path('ganaratescolarite',views.ganaratescolarite,name='ganaratescolarite'),
    #path('genaratepdf',views.generatepdf,name='generatepdf'),
    #path('adminScolarité/generate_pdr/',views.generate_pdr.as_view(), name='generate_pdr'),

      
      
]


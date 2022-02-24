from django.shortcuts import render

def index(request):
    return render(request, '../templates/registration/index.html')
def homeEtudiant(request):
    return render(request, '../templates/registration/etudiant_home.html')

def homeEProf(request):
    return render(request, '../templates/registration/prof_home.html') 



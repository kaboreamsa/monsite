from django.shortcuts import render, get_object_or_404
from .models import Projet

def projet_list(request):
    projets = Projet.objects.all()
    return render(request, 'portfolio/projet_list.html', {'projets': projets})

def projet_detail(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    return render(request, 'portfolio/projet_detail.html', {'projet': projet})
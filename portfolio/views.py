from django.shortcuts import render, get_object_or_404
from .models import Projet

def projet_list(request):
    projets = Projet.objects.all()
    return render(request, 'portfolio/projet_list.html', {'projets': projets})

def projet_detail(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    return render(request, 'portfolio/projet_detail.html', {'projet': projet})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjetForm

@login_required
def ajouter_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            projet = form.save()
            return redirect('portfolio:detail', pk=projet.pk)
    else:
        form = ProjetForm()
    return render(request, 'portfolio/ajouter_projet.html', {'form': form})
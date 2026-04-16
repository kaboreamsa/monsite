from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from blog.models import Article, Commentaire
from portfolio.models import Projet
from blog.forms import ArticleForm
from portfolio.forms import ProjetForm
from blog.forms import CommentaireForm  # à créer si nécessaire



def is_staff_user(user):
    return user.is_staff or user.is_superuser

def connexion(request):
    if request.user.is_authenticated:
        return redirect('dashboard:accueil')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and (user.is_staff or user.is_superuser):
            login(request, user)
            return redirect('dashboard:accueil')
        else:
            messages.error(request, 'Identifiants invalides ou vous n\'êtes pas autorisé.')
    return render(request, 'dashboard/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('dashboard:connexion')

@login_required
@user_passes_test(is_staff_user)
def accueil(request):
    #articles_non_approuves = Commentaire.objects.filter(approuve=False).count()
    commentaires_en_attente = Commentaire.objects.filter(approuve=False).count()
    context = {
        'total_articles': Article.objects.count(),
        'total_projets': Projet.objects.count(),
        'total_commentaires': Commentaire.objects.count(),
        'commentaires_attente': commentaires_en_attente,
    }
    return render(request, 'dashboard/accueil.html', context)

# Gestion des articles
@login_required
@user_passes_test(is_staff_user)
def liste_articles(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'dashboard/liste_articles.html', {'articles': articles})

@login_required
@user_passes_test(is_staff_user)
def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article ajouté avec succès.')
            return redirect('dashboard:liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'dashboard/ajouter_article.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def modifier_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article modifié.')
            return redirect('dashboard:liste_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'dashboard/modifier_article.html', {'form': form, 'article': article})

@login_required
@user_passes_test(is_staff_user)
def supprimer_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article supprimé.')
        return redirect('dashboard:liste_articles')
    return render(request, 'dashboard/supprimer_article.html', {'article': article})

# Gestion des projets (similaire)
@login_required
@user_passes_test(is_staff_user)
def liste_projets(request):
    projets = Projet.objects.all().order_by('-date_creation')
    return render(request, 'dashboard/liste_projets.html', {'projets': projets})

@login_required
@user_passes_test(is_staff_user)
def ajouter_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projet ajouté.')
            return redirect('dashboard:liste_projets')
    else:
        form = ProjetForm()
    return render(request, 'dashboard/ajouter_projet.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def modifier_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES, instance=projet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projet modifié.')
            return redirect('dashboard:liste_projets')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'dashboard/modifier_projet.html', {'form': form, 'projet': projet})

@login_required
@user_passes_test(is_staff_user)
def supprimer_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    if request.method == 'POST':
        projet.delete()
        messages.success(request, 'Projet supprimé.')
        return redirect('dashboard:liste_projets')
    return render(request, 'dashboard/supprimer_projet.html', {'projet': projet})

# Gestion des commentaires
@login_required
@user_passes_test(is_staff_user)
def liste_commentaires(request):
    commentaires = Commentaire.objects.all().order_by('-date_publication')
    return render(request, 'dashboard/liste_commentaires.html', {'commentaires': commentaires})

@login_required
@user_passes_test(is_staff_user)
def approuver_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    commentaire.approuve = True
    commentaire.save()
    messages.success(request, 'Commentaire approuvé.')
    return redirect('dashboard:liste_commentaires')

@login_required
@user_passes_test(is_staff_user)
def supprimer_commentaire(request, pk):
    commentaire = get_object_or_404(Commentaire, pk=pk)
    commentaire.delete()
    messages.success(request, 'Commentaire supprimé.')
    return redirect('dashboard:liste_commentaires')
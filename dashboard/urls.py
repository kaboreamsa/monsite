from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('', views.accueil, name='accueil'),
    
    # Articles
    path('articles/', views.liste_articles, name='liste_articles'),
    path('articles/ajouter/', views.ajouter_article, name='ajouter_article'),
    path('articles/modifier/<int:pk>/', views.modifier_article, name='modifier_article'),
    path('articles/supprimer/<int:pk>/', views.supprimer_article, name='supprimer_article'),
    
    # Projets
    path('projets/', views.liste_projets, name='liste_projets'),
    path('projets/ajouter/', views.ajouter_projet, name='ajouter_projet'),
    path('projets/modifier/<int:pk>/', views.modifier_projet, name='modifier_projet'),
    path('projets/supprimer/<int:pk>/', views.supprimer_projet, name='supprimer_projet'),
    
    # Commentaires
    path('commentaires/', views.liste_commentaires, name='liste_commentaires'),
    path('commentaires/approuver/<int:pk>/', views.approuver_commentaire, name='approuver_commentaire'),
    path('commentaires/supprimer/<int:pk>/', views.supprimer_commentaire, name='supprimer_commentaire'),
]
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'image']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 10}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['auteur', 'email', 'contenu']
        widgets = {
            'auteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'votre@email.com'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Votre commentaire...'}),
        }
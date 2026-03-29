from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication',)

from .models import Article, Commentaire

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'article', 'date_publication', 'approuve')
    list_filter = ('approuve', 'date_publication')
    search_fields = ('auteur', 'contenu')
    actions = ['approuver_commentaires']

    def approuver_commentaires(self, request, queryset):
        queryset.update(approuve=True)
    approuver_commentaires.short_description = "Approuver les commentaires sélectionnés"
from django.contrib import admin
from .models import Projet

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation')
    search_fields = ('titre',)
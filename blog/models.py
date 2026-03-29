from django.db import models
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_publication']


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)  # optionnel
    contenu = models.TextField()
    date_publication = models.DateTimeField(default=timezone.now)
    approuve = models.BooleanField(default=False)  # modération

    class Meta:
        ordering = ['date_publication']

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.article.titre}"
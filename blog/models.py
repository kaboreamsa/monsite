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
from django.db import models

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/')
    date_creation = models.DateField()

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_creation']
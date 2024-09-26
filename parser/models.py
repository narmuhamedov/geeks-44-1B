from django.db import models


class ManasFilm(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='parser/')
    time = models.CharField(max_length=30)

    def __str__(self):
        return self.title
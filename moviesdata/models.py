from django.db import models

# Create your models here.
class moviesdata(models.Model):
    title = models.CharField(max_length=70)
    released_year = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    generes = models.CharField(max_length=150)
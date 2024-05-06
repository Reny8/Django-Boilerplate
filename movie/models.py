from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    runtime = models.FloatField()
    rating = models.IntegerField()

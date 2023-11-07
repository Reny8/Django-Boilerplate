from django.db import models

# Create your models here.
RATING_CHOICES = {
    (1, 'G'),
    (2, 'PG'),
    (3, 'PG-13'),
    (4, 'R'),
    (5, 'NC-17')
}


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    runtime = models.FloatField()
    rating = models.IntegerField(choices=RATING_CHOICES)

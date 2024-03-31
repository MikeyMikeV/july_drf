from django.db import models
from django.core import validators

class Movie(models.Model):
    title = models.CharField(max_length=100)
    film_file = models.FileField(upload_to=f'movies/{title}/films', null = True)
    desc = models.TextField(null = True)
    release_date = models.DateField(null = True)
    poster = models.ImageField(upload_to=f'movies/{title}posters/',null = True, blank = True) 
    duration = models.DurationField(null = True)
    studio = models.CharField(max_length=100,null = True)
    rating = models.DecimalField(
        max_digits= 3, 
        decimal_places = 1, 
        validators = [
            validators.MinValueValidator(0), 
            validators.MaxValueValidator(10)
        ],
        default = 0
    )
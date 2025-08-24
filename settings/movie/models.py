from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    def __str__(self):
        return self.country_name

class Director(models.Model):
    name = models.CharField(max_length=100)
    director_image = models.ImageField()
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    actor_image = models.ImageField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True)
    movie_time = models.DurationField()
    description = models.TextField()
    movie_image = models.ImageField(upload_to='movies/')

    def __str__(self):
        return self.name

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return f"{self.movie.name} - {self.rating}/10"
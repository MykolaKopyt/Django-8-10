from django.db import models
from django.contrib.postgres.fields import ArrayField


class Movie(models.Model):
    class Title(models.TextChoices):
        SHORT = 'short', 'Short'
        MOVIE = 'movie', 'Movie'

    imdb_id = models.CharField('tconst', max_length=255, null=True)
    title_type = models.CharField('titleType', max_length=255, choices=Title.choices)
    name = models.CharField('primaryTitle', max_length=255)
    is_adult = models.BooleanField('isAdult')
    year = models.IntegerField('startYear', null=True)
    genres = ArrayField(models.CharField(max_length=255), null=True, verbose_name='Genres')

    def __str__(self):
        return self.name


class Person(models.Model):
    imdb_id = models.CharField('nconst', max_length=255, null=True)
    name = models.CharField('primaryName', max_length=255)
    birth_year = models.DateField('birthYear', null=True)
    death_year = models.DateField('deathYear', null=True)

    def __str__(self):
        return self.name


class PersonMovie(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    order = models.IntegerField('ordering', null=True)
    category = models.CharField("category", max_length=255, null=True)
    job = models.CharField('job', max_length=255, null=True)
    characters = ArrayField(models.CharField(max_length=255), verbose_name='Characters', null=True)


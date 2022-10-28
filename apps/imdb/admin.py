from django.contrib import admin
from .models import Movie, Person, PersonMovie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'imdb_id', 'name')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PersonMovie)
class PersonMovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'person_id', 'movie_id')

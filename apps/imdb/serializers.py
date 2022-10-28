from rest_framework import serializers
from .models import Person, Movie, PersonMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMovie
        fields = '__all__'

    movie = MovieSerializer()
    person = PersonSerializer()


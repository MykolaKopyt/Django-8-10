from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, FormView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.imdb.models import Movie, Person, PersonMovie
from apps.imdb.serializers import MovieSerializer, PersonSerializer


class MovieAPIList(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class PersonAPIList(ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

from django.urls import path

from .views import MovieAPIList, PersonAPIList

app_name = 'imdb.imdb'

urlpatterns = [
    path('movies/', MovieAPIList.as_view()),
    path('persons/', PersonAPIList.as_view()),

]
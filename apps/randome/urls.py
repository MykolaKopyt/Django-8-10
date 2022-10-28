from django.urls import path
from apps.randome.views import random_string

urlpatterns = [
    path('', random_string),
    path('random/', random_string)
]
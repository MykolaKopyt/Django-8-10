from django.urls import path
from apps.about.views import index, whoami

urlpatterns = [
    path('', index),
    path('about/', index),
    path('about/whoami/', whoami)
]
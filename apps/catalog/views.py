from rest_framework import viewsets
from .models import Developer, Genre, Console
from .serializer import DeveloperSerializer, GenreSerializer, ConsoleSerializer

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer

from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Developer
from .serializer import DeveloperSerializer, GenreSerializer, ConsoleSerializer

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
from django.shortcuts import render

# Create your views here.

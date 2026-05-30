from rest_framework import viewsets
from .models import Developer, Genre, Console, Game, Screenshot, Tag, GameTag
from .serializer import DeveloperSerializer, GenreSerializer, ConsoleSerializer, GameSerializer, ScreenshotSerializer, TagSerializer, GameTagSerializer

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class ScreenshotViewSet(viewsets.ModelViewSet):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class GameTagViewSet(viewsets.ModelViewSet):
    queryset = GameTag.objects.all()
    serializer_class = GameTagSerializer

from django.shortcuts import render


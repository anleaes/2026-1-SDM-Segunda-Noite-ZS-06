from rest_framework import viewsets, permissions
from .models import Genre
from .serializer import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    permission_classes = [permissions.IsAuthenticated]
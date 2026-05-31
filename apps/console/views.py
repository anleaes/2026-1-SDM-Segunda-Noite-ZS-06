from rest_framework import viewsets
from .models import Console
from .serializer import ConsoleSerializer

class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer
from rest_framework import viewsets, permissions
from .models import Console
from .serializer import ConsoleSerializer

class ConsoleViewSet(viewsets.ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer

    permission_classes = [permissions.IsAuthenticated]
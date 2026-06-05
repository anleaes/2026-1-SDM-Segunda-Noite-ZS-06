from rest_framework import viewsets
from .models import Tag, GameTag
from .serializer import TagSerializer, GameTagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # Adicione este método abaixo para associar o criador automaticamente:
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class GameTagViewSet(viewsets.ModelViewSet):
    queryset = GameTag.objects.all()
    serializer_class = GameTagSerializer

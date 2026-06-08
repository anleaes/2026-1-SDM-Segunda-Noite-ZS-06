from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import Tag, GameTag
from .serializer import TagSerializer, GameTagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # Só Admins criam categorias base (ex: "RPG", "Ação")
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Acesso Negado: Apenas administradores podem criar novas categorias de Tags.")
        serializer.save(created_by=self.request.user)

class GameTagViewSet(viewsets.ModelViewSet):
    serializer_class = GameTagSerializer

    def get_queryset(self):
        queryset = GameTag.objects.all()
        game_id = self.request.query_params.get('game', None)
        if game_id is not None:
            queryset = queryset.filter(game_id=game_id)
        return queryset
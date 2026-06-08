from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .models import Tag, GameTag
from .serializer import TagSerializer, GameTagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # REGRA 1: Só Administradores criam Tags Base
    def perform_create(self, serializer):
        if not self.request.user.is_staff: # Verifica se é admin no Django
            raise PermissionDenied("Acesso Negado: Apenas administradores podem criar novas categorias de Tags.")
        
        # Carimba quem foi o admin que criou
        serializer.save(created_by=self.request.user)


class GameTagViewSet(viewsets.ModelViewSet):
    serializer_class = GameTagSerializer

    # Permite buscar as tags de um jogo específico (/tag/gametag/?game=5)
    def get_queryset(self):
        queryset = GameTag.objects.all()
        game_id = self.request.query_params.get('game', None)
        if game_id is not None:
            queryset = queryset.filter(game_id=game_id)
        return queryset

    # REGRA 2: Só o dono do jogo adiciona a Tag nele
    def perform_create(self, serializer):
        jogo = serializer.validated_data['game']
        if jogo.added_by != self.request.user:
            raise PermissionDenied("Acesso Negado: Você só pode adicionar tags aos jogos que você mesmo cadastrou.")
        serializer.save()

    # REGRA 3: Só o dono do jogo remove a Tag dele
    def perform_destroy(self, instance):
        if instance.game.added_by != self.request.user:
            raise PermissionDenied("Acesso Negado: Você só pode remover tags dos jogos que você mesmo cadastrou.")
        instance.delete()
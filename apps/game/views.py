from rest_framework import viewsets
from .models import Game, Screenshot
from .serializer import GameSerializer, ScreenshotSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class ScreenshotViewSet(viewsets.ModelViewSet):
    serializer_class = ScreenshotSerializer

    def get_queryset(self):
        queryset = Screenshot.objects.all()
        
        # Permite que o app peça as fotos apenas do jogo atual
        game_id = self.request.query_params.get('game', None)
        if game_id is not None:
            queryset = queryset.filter(game_id=game_id)
            
        # A CORREÇÃO: Garante que a lista volte ordenada da foto mais antiga para a mais nova
        return queryset.order_by('upload_date')
    

    def perform_create(self, serializer):
        jogo = serializer.validated_data['game']
        
        # Verifica se o ID do usuário que mandou a requisição é igual ao ID do criador do jogo
        if jogo.added_by != self.request.user:
            raise PermissionDenied("Acesso negado: Você só pode adicionar fotos aos jogos que você mesmo cadastrou.")
        
        serializer.save()

    # 2. O SEGURANÇA DA EXCLUSÃO:
    def perform_destroy(self, instance):
        # O 'instance' é a foto que está tentando ser apagada. Olhamos para o dono do jogo dela.
        if instance.game.added_by != self.request.user:
            raise PermissionDenied("Acesso negado: Você só pode apagar fotos dos jogos que você mesmo cadastrou.")
        
        instance.delete()
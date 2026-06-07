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
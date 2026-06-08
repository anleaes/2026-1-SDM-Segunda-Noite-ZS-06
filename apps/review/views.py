from rest_framework import viewsets
from .models import Review
from .serializer import ReviewSerializer
from users.models import User

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        # Essa linha permite que o React Native peça: "Me dê só as reviews do jogo ID 5" (/reviews/?game=5)
        game_id = self.request.query_params.get('game', None)
        if game_id is not None:
            queryset = queryset.filter(game_id=game_id)
        
        # Ordena para as mais recentes aparecerem primeiro
        return queryset.order_by('-review_date')

    def perform_create(self, serializer):
        usuario_real = User.objects.get(id=self.request.user.id)
        jogo_avaliado = serializer.validated_data['game']
        
        # A MÁGICA AQUI: Se já existe uma review desse usuário para este jogo, nós apagamos a antiga!
        Review.objects.filter(user=usuario_real, game=jogo_avaliado).delete()
        
        # Salva a nova review
        serializer.save(user=usuario_real)

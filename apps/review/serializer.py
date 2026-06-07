from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    # Puxa o nome do usuário para podermos mostrar na tela do app
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        # Listamos explicitamente para garantir que o 'username' seja incluído
        fields = ['id', 'game', 'user', 'rating', 'comment', 'review_date', 'recommended', 'username']
        
        # A SOLUÇÃO DO ERRO 400: Avisamos o Django que ele NÃO DEVE cobrar o usuário na entrada, 
        # pois nós vamos preenchê-lo manualmente lá na View.
        read_only_fields = ['user', 'review_date']
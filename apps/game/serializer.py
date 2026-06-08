from rest_framework import serializers
from .models import Game, Screenshot

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

    def to_representation(self, instance):
        # Pega a resposta padrão (só com os IDs)
        response = super().to_representation(instance)
        
        # Substitui o ID da desenvolvedora pelo objeto com ID e Nome
        if instance.developer:
            response['developer'] = {
                'id': instance.developer.id,
                'name': instance.developer.name
            }
            
        # Transforma a lista de IDs de gêneros numa lista de objetos
        response['genre'] = [
            {'id': genero.id, 'name': genero.name} for genero in instance.genre.all()
        ]
        
        # Transforma a lista de IDs de consoles numa lista de objetos
        response['consoles'] = [
            {'id': console.id, 'name': console.name} for console in instance.consoles.all()
        ]
        
        return response    

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ['id', 'game', 'image']
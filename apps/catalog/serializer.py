from rest_framework import serializers
from .models import Developer, Genre, Console, Game

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ConsoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Console
        fields = '__all__'
    
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
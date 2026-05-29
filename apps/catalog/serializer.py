from rest_framework import serializers
from .models import Developer, Genre, Console, Game, Review, Screenshot, Tag, GameTag


    
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


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

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class GameTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameTag
        fields = '__all__'
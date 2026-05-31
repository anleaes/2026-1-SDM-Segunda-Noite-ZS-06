from rest_framework import serializers
from .models import Tag, GameTag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class GameTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameTag
        fields = '__all__'
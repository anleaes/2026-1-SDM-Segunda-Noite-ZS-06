from rest_framework import serializers
from .models import Tag, GameTag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['created_by']

class GameTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameTag
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        
        # Expande a Tag para o React Native poder ler o nome dela facilmente
        if instance.tag:
            response['tag_details'] = {
                'id': instance.tag.id,
                'name': instance.tag.name,
                'category': instance.tag.category
            }
            
        return response

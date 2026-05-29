from .models import User, UserProfile
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'avatar', 'bio', 'country', 'games_added'] # ao invés de '__all__', estou configurando isso, não mexe
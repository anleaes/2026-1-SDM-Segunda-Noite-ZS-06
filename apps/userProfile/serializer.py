from .models import User, UserProfile
from rest_framework import serializers
from users.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'avatar', 'bio', 'country', 'games_added', 'username'] # ao invés de '__all__'
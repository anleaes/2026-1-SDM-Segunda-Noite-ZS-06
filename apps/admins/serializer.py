from .models import Admin
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        # 'is_superuser' no final da lista
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'username', 'password', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_staff'] = True
        validated_data['is_superuser'] = True # <-- A MÁGICA ACONTECE AQUI
        
        return super().create(validated_data)
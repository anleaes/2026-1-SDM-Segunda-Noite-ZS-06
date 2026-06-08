from .models import Admin
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        validated_data['password'] = make_password(validated_data['password'])
        
        validated_data['is_staff'] = True 
        
        return super().create(validated_data)
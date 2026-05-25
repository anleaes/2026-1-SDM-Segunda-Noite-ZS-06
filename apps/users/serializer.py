from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        
        # Cria a instância com o restante dos dados
        instance = self.Meta.model(**validated_data)

        if password is not None:
            # Encripta a senha
            instance.set_password(password)
        
        instance.save()
        return instance
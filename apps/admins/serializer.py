from .models import Admin
from rest_framework import serializers

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Remove a senha dos dados brutos
        password = validated_data.pop('senha', None)
        # Cria o objeto do usuário sem a senha primeiro
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            # Encriptação da senha
            instance.set_password(password)
        
        instance.save()
        return instance
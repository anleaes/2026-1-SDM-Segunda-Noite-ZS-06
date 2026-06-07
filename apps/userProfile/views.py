from django.shortcuts import render
from .models import UserProfile
from rest_framework import viewsets
from .serializer import UserProfileSerializer
from users.models import User
from rest_framework.response import Response

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer  
    
    def get_queryset(self):
        user = self.request.user 
        # Para usuários comuns, tenta filtrar. Se der erro de tipo, retorna vazio.
        try:
            return UserProfile.objects.filter(user__id=user.id)
        except ValueError:
            return UserProfile.objects.none()
        

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        # Se o banco retornar vazio, o usuário não tem perfil salvo ainda:
        if not queryset.exists():
            usuario_real = User.objects.get(id=request.user.id)
            # Cria um perfil em branco ligado a ele
            UserProfile.objects.create(user=usuario_real)
            # Busca a lista de novo, com o perfil recém criado
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



    
    def perform_create(self, serializer):
        usuario_real = User.objects.get(id=self.request.user.id)
        # Isso daqui salva o perfil pra logar automaticamente, acho que funcionda
        serializer.save(user=usuario_real)

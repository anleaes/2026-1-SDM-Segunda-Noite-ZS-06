from django.shortcuts import render
from .models import UserProfile
from rest_framework import viewsets
from .serializer import UserProfileSerializer
from users.models import User

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
    
    def perform_create(self, serializer):
        usuario_real = User.objects.get(id=self.request.user.id)
        # Isso daqui salva o perfil pra logar automaticamente, acho que funcionda
        serializer.save(user=usuario_real)

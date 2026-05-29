from django.shortcuts import render
from .models import UserProfile
from rest_framework import viewsets
from .serializer import UserProfileSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    #apaguei o queryset, preciso colocar outras informações pra manter a função de login funcional
    serializer_class = UserProfileSerializer  
    
    def get_queryset(self):
        user = self.request.user
        # Se for um superusuário (Admin), ele vê todos os perfis para não dar erro
        if user.is_superuser:
            return UserProfile.objects.all()
        
        # Para usuários comuns, tenta filtrar. Se der erro de tipo, retorna vazio.
        try:
            return UserProfile.objects.filter(user=user)
        except ValueError:
            return UserProfile.objects.none()
    
    def perform_create(self, serializer):
        # Isso daqui salva o perfil pra logar automaticamente, acho que funcionda
        serializer.save(user=self.request.user)

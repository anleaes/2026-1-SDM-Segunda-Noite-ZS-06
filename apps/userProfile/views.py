from django.shortcuts import render
from .models import UserProfile
from rest_framework import viewsets
from .serializer import UserProfileSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    #apaguei o queryset, preciso colocar outras informações pra manter a função de login funcional
    serializer_class = UserProfileSerializer  
    
    def get_queryset(self):
        # Essa linha faz com que o usuário veja só o perfil dele, acho que tá funcionando
        return UserProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Isso daqui salva o perfil pra logar automaticamente, acho que funcionda
        serializer.save(user=self.request.user)

from django.shortcuts import render
from .models import UserProfile
from rest_framework import viewsets, permissions
from .serializer import UserProfileSerializer
from users.models import User
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError # <-- IMPORTAÇÃO NOVA PARA BARRAR O ERRO

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer  
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            usuario_real = User.objects.get(id=self.request.user.id)
            return UserProfile.objects.filter(user=usuario_real)
        except User.DoesNotExist:
            return UserProfile.objects.none()
        
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        try:
            usuario_real = User.objects.get(id=request.user.id)
            is_usuario_comum = True
        except User.DoesNotExist:
            is_usuario_comum = False

        if not queryset.exists() and is_usuario_comum:
            UserProfile.objects.create(user=usuario_real)
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        try:
            # Tenta encontrar o usuário comum para salvar o perfil
            usuario_real = User.objects.get(id=self.request.user.id)
            serializer.save(user=usuario_real)
        except User.DoesNotExist:
            # Se for o Administrador tentando salvar, barra a ação sem quebrar o servidor
            raise ValidationError({"detail": "Contas de Administrador não possuem perfil de jogador."})
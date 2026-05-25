from django.shortcuts import render
from .models import User
from rest_framework import viewsets, permissions
from .serializer import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()] # Libera pra criar a conta
        return [permissions.IsAuthenticated()] # Bloqueia o resto, a ideia é que sem uma conta, tu tenha apenas a aba de criação de conta liberada
from django.shortcuts import render
from .models import Admin
from rest_framework import viewsets, permissions
from .serializer import AdminSerializer


# Create your views here.
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer  

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()] # Libera pra cirar conta de admin
        return [permissions.IsAuthenticated()] # Tranca todas outras abas, a ideia é que sem login, esteja tudo trancado, menos a aba de criar conta
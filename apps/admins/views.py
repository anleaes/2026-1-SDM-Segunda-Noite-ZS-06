from django.shortcuts import render
from .models import Admin
from rest_framework import viewsets, permissions
from .serializer import AdminSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def get_permissions(self):
        if self.action in ['create']: # Libera só a criação para quem não tem login
            return [AllowAny()]
        return [IsAuthenticated()]
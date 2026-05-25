from django.shortcuts import render
from .models import Admin
from rest_framework import viewsets, permissions
from .serializer import AdminSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
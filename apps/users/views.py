from django.shortcuts import render
from .models import User
from rest_framework import viewsets, permissions
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [] 
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
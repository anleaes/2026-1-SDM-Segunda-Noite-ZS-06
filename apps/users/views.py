from django.shortcuts import render
from .models import User
from rest_framework import viewsets, permissions
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'list']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    
@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) 
def logout_view(request):
    logout(request)
    return redirect('/api-auth/login/')
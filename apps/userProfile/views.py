from django.shortcuts import render
from .models import UserProfile
from rest_framework import viewsets
from .serializer import UserProfileSerializer

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer  


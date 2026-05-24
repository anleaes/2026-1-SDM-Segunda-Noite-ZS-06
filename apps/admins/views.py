from django.shortcuts import render
from .models import Admin
from rest_framework import viewsets
from .serializer import AdminSerializer


# Create your views here.
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer  
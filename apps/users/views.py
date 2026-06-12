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

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from apps.userProfile.models import UserProfile
from .forms import UserRegisterForm

def traditional_login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('game:list_games_view')
        else:
            return render(request, 'accounts/user_login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'accounts/user_login.html')

def traditional_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            # Garante que o perfil do usuário seja instanciado em branco
            UserProfile.objects.get_or_create(user=user)
            return redirect('users:traditional_login_view')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/add_user.html', {'form': form})

def traditional_logout_view(request):
    logout(request)
    return redirect('users:traditional_login_view')

@login_required(login_url='/usuarios/login/')
def traditional_profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        country = request.POST.get('country')
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.bio = bio
        profile.country = country
        profile.save()
        return redirect('users:traditional_profile_view')
    return render(request, 'accounts/user_profile.html', {'profile': profile})
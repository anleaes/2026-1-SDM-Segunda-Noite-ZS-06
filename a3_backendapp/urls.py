from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from users.views import logout_view 
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import redirect

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# ---> A FERRAMENTA DEFINITIVA PARA BUSCAR MODELOS <---
from django.apps import apps 

@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({'detail': 'CSRF cookie set'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    # Em vez de importar o arquivo, pedimos o modelo direto pro coração do Django:
    Admin = apps.get_model('admins', 'Admin')

    # O Django vai olhar na sua tabela Admin para ver se o usuário logado existe lá
    is_custom_admin = Admin.objects.filter(username=request.user.username).exists()

    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'is_admin': is_custom_admin # Esta é a nova flag que o Vue vai ler
    })

urlpatterns = [
     path('', lambda request: redirect('game:list_games_view')),
    path('admin/', admin.site.urls),
    path('api/set-csrf-cookie/', set_csrf_token, name='set-csrf-cookie'),
    path('api-auth/logout/', logout_view, name='logout'),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/token/', obtain_auth_token, name='api_token_auth'),

    path('api/me/', get_current_user, name='current-user'),
   
    path('pessoas/', include('persons.urls', namespace='persons')),
    path('usuarios/', include('users.urls', namespace='users')),
    path('jogos/', include('apps.game.urls', namespace='game')),
    path('developer/', include('apps.developer.urls', namespace='developer')),
    path('genre/', include('apps.genre.urls', namespace='genre')),
    path('console/', include('apps.console.urls', namespace='console')),
    path('review/', include('apps.review.urls', namespace='review')),
    path('tag/', include('apps.tag.urls', namespace='tag')),
    path('administradores/', include('admins.urls', namespace='admins')),
    path('perfil/', include('userProfile.urls', namespace='userProfile')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
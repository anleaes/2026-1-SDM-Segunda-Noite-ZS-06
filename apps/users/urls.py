from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'users'

router = routers.SimpleRouter()
router.register('', views.UserViewSet, basename='usuarios')

urlpatterns = [
    # Rotas tradicionais de templates HTML para o Frontend
    path('login/', views.traditional_login_view, name='traditional_login_view'),
    path('cadastrar/', views.traditional_register_view, name='traditional_register_view'),
    path('sair/', views.traditional_logout_view, name='traditional_logout_view'),
    path('perfil/', views.traditional_profile_view, name='traditional_profile_view'),
    
    # Endpoints do DRF para o Vue/React Native
    path('', include(router.urls) )
]
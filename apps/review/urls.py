from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'review'
router = routers.SimpleRouter()

# Registra o ViewSet. O caminho vazio '' significa que ele vai responder na raiz da URL que você definiu no projeto principal.
router.register('', views.ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
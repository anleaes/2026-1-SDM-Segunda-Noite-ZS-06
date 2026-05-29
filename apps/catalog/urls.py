from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'catalog'

router = DefaultRouter()
# Rotas registradas:
router.register(r'game', views.GameViewSet, basename='game')
router.register(r'developer', views.DeveloperViewSet, basename='developer')
router.register(r'genre', views.GenreViewSet, basename='genre')
router.register(r'console', views.ConsoleViewSet, basename='console')
router.register(r'screenshot', views.ScreenshotViewSet, basename='screenshot')

urlpatterns = [
    path('', include(router.urls)),
]
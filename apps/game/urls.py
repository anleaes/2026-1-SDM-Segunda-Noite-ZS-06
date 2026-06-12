from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

app_name = 'game'

router = routers.SimpleRouter()
router.register('screenshot', views.ScreenshotViewSet, basename='screenshot')
router.register('', views.GameViewSet, basename='game')

urlpatterns = [
    path('ver/<int:id_game>/', views.view_game_view, name='view_game_view'),
    path('screenshot/excluir/<int:id_screenshot>/', views.delete_screenshot_view, name='delete_screenshot_view'),
    path('listar/', views.list_games_view, name='list_games_view'),
    path('adicionar/', views.add_game_view, name='add_game_view'),
    path('editar/<int:id_game>/', views.edit_game_view, name='edit_game_view'),
    path('excluir/<int:id_game>/', views.delete_game_view, name='delete_game_view'),
    path('', include(router.urls)),
]
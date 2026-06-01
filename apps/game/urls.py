from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

app_name = 'game'

router = routers.SimpleRouter()
router.register('', views.GameViewSet, basename='game')
router.register(r'screenshot', views.ScreenshotViewSet, basename='screenshot')

urlpatterns = [
    path('', include(router.urls)),
]
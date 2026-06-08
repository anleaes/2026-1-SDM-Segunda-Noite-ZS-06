from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

app_name = 'game'

router = routers.SimpleRouter()
router.register('screenshot', views.ScreenshotViewSet, basename='screenshot')
router.register('', views.GameViewSet, basename='game')

urlpatterns = [
    path('', include(router.urls)),
]
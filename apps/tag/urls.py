from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

app_name = 'tag'
router = routers.SimpleRouter()
router.register('', views.TagViewSet, basename='tag')
router.register(r'gametag', views.GameTagViewSet, basename='gametag')

urlpatterns = [
    path('', include(router.urls)),
]
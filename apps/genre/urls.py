from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

app_name = 'genre'
router = routers.SimpleRouter()
router.register('', views.GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
]
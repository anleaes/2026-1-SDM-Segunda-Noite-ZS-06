from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'genre'
router = DefaultRouter()
router.register(r'genre', views.GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
]
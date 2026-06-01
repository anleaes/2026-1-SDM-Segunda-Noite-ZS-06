from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

app_name = 'console'
router = routers.SimpleRouter()
router.register('', views.ConsoleViewSet, basename='console')

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

app_name = 'developer'
router = routers.SimpleRouter()
router.register(r'developer', views.DeveloperViewSet, basename='developer')

urlpatterns = [
    path('', include(router.urls)),
]
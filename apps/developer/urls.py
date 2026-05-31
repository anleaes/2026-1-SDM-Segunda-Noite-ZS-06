from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'developer'
router = DefaultRouter()
router.register(r'developer', views.DeveloperViewSet, basename='developer')

urlpatterns = [
    path('', include(router.urls)),
]
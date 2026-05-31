from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'console'
router = DefaultRouter()
router.register(r'console', views.ConsoleViewSet, basename='console')

urlpatterns = [
    path('', include(router.urls)),
]
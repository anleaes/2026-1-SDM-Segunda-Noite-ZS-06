from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'tag'
router = DefaultRouter()
router.register(r'tag', views.TagViewSet, basename='tag')
router.register(r'gametag', views.GameTagViewSet, basename='gametag')

urlpatterns = [
    path('', include(router.urls)),
]
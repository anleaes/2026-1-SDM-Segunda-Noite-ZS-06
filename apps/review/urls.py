from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

app_name = 'review'
router = routers.SimpleRouter()
router.register(r'review', views.ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
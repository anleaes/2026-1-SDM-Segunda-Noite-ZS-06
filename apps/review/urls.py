from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'review'
router = DefaultRouter()
router.register(r'review', views.ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
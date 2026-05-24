from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'users'

router = routers.SimpleRouter()
router.register('', views.UserViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls) )
]
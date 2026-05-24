from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'userProfiles'

router = routers.SimpleRouter()
router.register('', views.UserProfileViewSet, basename='perfil de usuario')

urlpatterns = [
    path('', include(router.urls) )
]
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'employees'

router = routers.SimpleRouter()
router.register('', views.AdminViewSet, basename='administradores')

urlpatterns = [
    path('', include(router.urls) )
]
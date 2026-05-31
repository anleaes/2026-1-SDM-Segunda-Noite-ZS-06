"""
URL configuration for a3_backendapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from users.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/logout/', logout_view, name='logout'),
     path('api-auth/', include('rest_framework.urls')), # permite o login no canto superior direito, estou trabalhando pra fazer isso dar certo, não mexe nisso
    path('pessoas/', include('persons.urls', namespace='persons')),
    path('usuarios/', include('users.urls', namespace='users')),
    path('jogos/', include('apps.game.urls', namespace='game')),
    path('developer/', include('apps.developer.urls', namespace='developer')),
    path('genre/', include('apps.genre.urls', namespace='genre')),
    path('console/', include('apps.console.urls', namespace='console')),
    path('review/', include('apps.review.urls', namespace='review')),
    path('tag/', include('apps.tag.urls', namespace='tag')),
    path('administradores/', include('admins.urls', namespace='admins')),
    path('perfis de usuarios/', include('userProfile.urls', namespace='userProfile')),
]

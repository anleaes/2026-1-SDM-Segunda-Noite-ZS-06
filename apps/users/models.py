from django.db import models
from persons.models import Person

# Create your models here.
class User(Person):
    username = models.CharField('Usuário', max_length=50, unique=True)
    password = models.CharField('Senha', max_length=128) 
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    is_active = models.BooleanField('Ativo', default=True)
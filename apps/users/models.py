from django.db import models
from persons.models import Person
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(Person):
    username = models.CharField('Usuário', max_length=50, unique=True)
    password = models.CharField('Senha', max_length=128) 
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    is_active = models.BooleanField('Ativo', default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']

    def __str__(self):
        return self.username
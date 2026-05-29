from django.db import models
from persons.models import Person
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class Admin(Person):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        ordering = ['username']

    def __str__(self):
        return self.username
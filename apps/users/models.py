from django.db import models
from persons.models import Person
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('O usuário deve ter um nome')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True 
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)

class User(Person):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']

    def __str__(self):
        return self.username
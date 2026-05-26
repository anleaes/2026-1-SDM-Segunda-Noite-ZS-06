from django.db import models
from persons.models import Person
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import check_password, make_password

# Create your models here.
class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class Admin(Person):
    username = models.CharField('Usuário', max_length=50, unique=True)
    password = models.CharField('Senha', max_length=128) 
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    is_active = models.BooleanField('Ativo', default=True)

    objects = UserManager()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    is_staff = True  
    is_active = True 
    
    def has_perm(self, perm, obj=None): return True
    def has_module_perms(self, app_label): return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        ordering = ['username']

    def __str__(self):
        return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Person(AbstractUser):
    #Esses atributos vem do AbstractUser, coloquei aqui pra exemplificar o models do Persons

    #first_name = models.CharField('Nome', max_length=50)
    #last_name = models.CharField('Sobrenome', max_length=100)
    # #email = models.EmailField('E-mail',null=False, blank=False)

    birth_date = models.DateField('Data de Nascimento', null=True, blank=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering =['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100)
    birth_date = models.DateField('Data de Nascimento', null=True, blank=True)
    email = models.EmailField('E-mail',null=False, blank=False)

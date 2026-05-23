from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100)
    birth_date = models.DateField('Data de Nascimento', null=True, blank=True)
    email = models.EmailField('E-mail',null=False, blank=False)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering =['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

from django.db import models
from users.models import User

# Create your models here.
class UserProfile(models.Model):
    avatar = models.ImageField('Avatar', upload_to='avatars/', null=True, blank=True)
    bio = models.TextField('Biografia', max_length=2000, blank=True)
    country = models.CharField('País', max_length=100)
    games_added = models.IntegerField('Jogos Adicionados', default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Perfil de Usuário'
        verbose_name_plural = 'Perfis de Usuários'

    def __str__(self):
        return f'Perfil de {self.user.username}'

   

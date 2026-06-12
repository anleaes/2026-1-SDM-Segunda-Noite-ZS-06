from django.db import models
from django.conf import settings

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField()
    cover_image = models.ImageField(upload_to='games/', blank=True, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='games_added', null=True, blank=True)
    
    developer = models.ForeignKey('developer.Developer', on_delete=models.CASCADE, related_name='games')
    genre = models.ManyToManyField('genre.Genre', related_name='games')
    consoles = models.ManyToManyField('console.Console', related_name='games')

    class Meta:
        db_table = 'catalog_game'


    def __str__(self):
        return self.title

class Screenshot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='screenshots/')
    description = models.TextField(blank=True, null=True)
    is_thumbnail = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'catalog_screenshot'
        app_label = 'screenshot'

    def __str__(self):
        return f"{self.game.title} - Screenshot {self.id}"
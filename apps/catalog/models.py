from django.db import models
from django.conf import settings

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField()
    cover_image = models.ImageField(upload_to='games/', blank=True, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    
    # As aspas salvam a vida e evitam o NameError:
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE, related_name='games')
    genre = models.ManyToManyField('Genre', related_name='games')
    consoles = models.ManyToManyField('Console', related_name='games')

    def __str__(self):
        return self.title

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    foundation_year = models.IntegerField()
    description = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    difficulty = models.CharField(max_length=50, blank=True, null=True)
    common_elements = models.TextField(blank=True, null=True)

class Console(models.Model):
    name = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=100)
    release_year = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Screenshot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='screenshots/')
    description = models.TextField(blank=True, null=True)
    is_thumbnail = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    recommended = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.game.title} - Screenshot {self.id}"

    def __str__(self):
        return f"Review de {self.user.username} para {self.game.title}"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GameTag(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='gametags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='gametags')
    added_date = models.DateTimeField(auto_now_add=True)
    is_primary = models.BooleanField(default=False)
    is_spoiler = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.game.title} - {self.tag.name}"
from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_tags')

    class Meta:
        db_table = 'catalog_tag'

    def __str__(self):
        return self.name

class GameTag(models.Model):
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='gametags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='gametags')
    added_date = models.DateTimeField(auto_now_add=True)
    is_primary = models.BooleanField(default=False)
    is_spoiler = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)

    class Meta:
        db_table = 'catalog_gametag'

    def __str__(self):
        return f"{self.game.title} - {self.tag.name}"
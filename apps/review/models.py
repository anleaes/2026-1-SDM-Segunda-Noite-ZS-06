from django.db import models
from django.conf import settings

class Review(models.Model):
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)
    recommended = models.BooleanField(default=True)

    class Meta:
        db_table = 'catalog_review'

    def __str__(self):
        return f"{self.game.title} - {self.user}"
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'catalog_genre'

    def __str__(self):
        return self.name
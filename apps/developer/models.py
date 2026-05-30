from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    foundation_year = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'catalog_developer'

    def __str__(self):
        return self.name
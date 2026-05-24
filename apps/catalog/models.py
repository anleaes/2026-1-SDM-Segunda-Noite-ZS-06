from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    foundation_year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
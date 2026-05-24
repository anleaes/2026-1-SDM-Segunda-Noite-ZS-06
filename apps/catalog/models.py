from django.db import models

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
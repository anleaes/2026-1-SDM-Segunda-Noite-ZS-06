from django.db import models

class Console(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    release_year = models.IntegerField()

    class Meta:
        db_table = 'catalog_console'
        app_label = 'console'

    def __str__(self):
        return self.name
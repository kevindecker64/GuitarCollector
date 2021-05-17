from django.db import models

# Create your models here.
class Guitar(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.model
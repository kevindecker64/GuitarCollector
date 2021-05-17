from django.db import models
from django.urls import reverse

# Create your models here.
class Guitar(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("detail", kwargs={"guitar_id": self.id})
    
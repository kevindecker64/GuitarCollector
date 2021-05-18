from django.db import models
from django.urls import reverse

SERVICES = (
    ("F", "Full Set-Up"),
    ("C", "Cleaning"),
    ("N", "Neck + Truss Rod Adjustment"),
    ("P", "Pick-Ups Adjustment"),
    ("S", "New Strings"),
)

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


class SetUp(models.Model):
    date = models.DateField("Set-Up Date")
    service = models.CharField(max_length=1, choices=SERVICES, default=SERVICES[0][0])
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}: {self.get_service_display()} on {self.guitar.model}"

    class Meta:
        ordering = ['-date']
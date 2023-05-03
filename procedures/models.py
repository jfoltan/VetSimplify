from django.db import models


# Create your models here.
class Procedure(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=50)
    margin = models.IntegerField(validators=[MinValueValidator(0)])
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class StockItem(models.Model):
    TYPE_CHOICES = [
        ("CURE", "Lék"),
        ("MATERIAL", "Materiál"),
        ("OTHER", "Ostatní"),
    ]

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True, null=True)
    supplier_code = models.CharField(max_length=50, blank=True, null=True)
    supplier = models.CharField(max_length=200, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    ean = models.CharField(max_length=50, blank=True, null=True)
    batch = models.CharField(max_length=50, blank=True, null=True)
    units_in_stock = models.DecimalField(max_digits=10, decimal_places=2)
    units_in_package = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.IntegerField(validators=[MinValueValidator(0)])
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + " [" + str(self.units_in_stock) + "]"

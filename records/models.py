from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = CountryField(blank_label="(vyberte zemi)")
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    ic = models.CharField(max_length=20, blank=True)
    dic = models.CharField(max_length=20, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

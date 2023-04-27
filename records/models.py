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


class Animal(models.Model):
    ANIMAL_TYPE_CHOICES = [
        ("dog", "Pes"),
        ("cat", "Kočka"),
        ("rodent", "Hlodavec"),
        ("bird", "Pták"),
        ("horse", "Kůň"),
        ("reptile", "Plaz"),
        ("pig", "Prase"),
        ("sheep", "Ovce"),
        ("goat", "Koza"),
        ("cow", "Kráva"),
        ("other", "Jiné"),
    ]

    GENDER_CHOICES = [
        ("male", "Samec"),
        ("female", "Samice"),
        ("unknown", "Neznámé"),
    ]

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="animals")
    name = models.CharField(max_length=50)
    animal_type = models.CharField(
        max_length=10, choices=ANIMAL_TYPE_CHOICES, default="dog"
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    breed = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    chip_number = models.CharField(max_length=50, blank=True)
    chip_location = models.CharField(max_length=50, blank=True)
    chip_application_date = models.DateField(blank=True, null=True)
    passport_number = models.CharField(max_length=50, blank=True)
    passport_issue_date = models.DateField(blank=True, null=True)
    castration = models.BooleanField(default=False)
    dead = models.BooleanField(default=False)
    insured = models.BooleanField(default=False)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.animal_type})"

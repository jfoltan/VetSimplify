from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.animal_type})"


class AnimalCase(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="cases")
    name = models.CharField(max_length=50)
    closed = models.BooleanField(default=False)
    closed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.closed and self.closed_at is None:
            self.closed_at = timezone.now()
        elif not self.closed:
            self.closed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.animal.name})"


class Visit(models.Model):
    animal_case = models.ForeignKey(
        AnimalCase, on_delete=models.CASCADE, related_name="visits"
    )
    weight = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    record = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Návštěva {self.created_at} ({self.animal_case.animal.name})"

    def calculate_price(self):
        stock_items_total = sum(item.price for item in self.stock_items.all())
        procedures_total = sum(procedure.price for procedure in self.procedures.all())
        self.price = stock_items_total + procedures_total
        self.save()


class VisitStockItem(models.Model):
    visit = models.ForeignKey(
        Visit, on_delete=models.CASCADE, related_name="stock_items"
    )
    stock_item = models.ForeignKey("stock.StockItem", on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.visit.calculate_price()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.visit.calculate_price()


class VisitProcedure(models.Model):
    visit = models.ForeignKey(
        Visit, on_delete=models.CASCADE, related_name="procedures"
    )
    procedure = models.ForeignKey("procedures.Procedure", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.visit.calculate_price()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.visit.calculate_price()

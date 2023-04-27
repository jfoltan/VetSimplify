from django.contrib import admin
from .models import Owner, Animal


# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "company_name",
        "ic",
        "dic",
        "created_at",
        "updated_at",
    )


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "animal_type",
        "gender",
        "date_of_birth",
    )

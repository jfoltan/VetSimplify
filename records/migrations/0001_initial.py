# Generated by Django 4.2 on 2023-04-27 12:21

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=50)),
                ("house_number", models.CharField(max_length=10)),
                ("city", models.CharField(max_length=50)),
                ("postal_code", models.CharField(max_length=10)),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("phone_number", models.CharField(blank=True, max_length=20)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("company_name", models.CharField(blank=True, max_length=50)),
                ("ic", models.CharField(blank=True, max_length=20)),
                ("dic", models.CharField(blank=True, max_length=20)),
                ("note", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
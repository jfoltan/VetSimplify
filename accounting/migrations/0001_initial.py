# Generated by Django 4.2 on 2023-05-05 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("records", "0004_visit_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                ("generated_at", models.DateTimeField(auto_now_add=True)),
                ("content", models.BinaryField()),
                (
                    "visit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="records.visit"
                    ),
                ),
            ],
        ),
    ]

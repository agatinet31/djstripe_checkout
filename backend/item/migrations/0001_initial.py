# Generated by Django 4.2.10 on 2024-03-03 20:35

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Required. 3-150 characters. Letters, digit.",
                        max_length=150,
                        validators=[
                            django.core.validators.MinLengthValidator(3),
                            django.core.validators.RegexValidator(
                                re.compile("^[^\\W\\d_][\\w \\-()]+$"),
                                "Enter a valid `name` value consisting of only letters, digit. and symbols _ ( )The first symbol only letter.",
                                "invalid",
                            ),
                        ],
                        verbose_name="name",
                    ),
                ),
                (
                    "price",
                    models.CharField(
                        help_text="Required. 100 characters.",
                        max_length=100,
                        unique=True,
                        verbose_name="price",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Not required. Description for item.",
                        max_length=250,
                        null=True,
                        verbose_name="description",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ("name",),
            },
        ),
    ]

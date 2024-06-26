# Generated by Django 4.1.2 on 2024-05-31 05:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Voucher",
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
                ("code", models.CharField(max_length=12, unique=True)),
                (
                    "discount_type",
                    models.CharField(
                        choices=[("percentage", "%"), ("fixed_amount", "VND")],
                        max_length=12,
                    ),
                ),
                ("discount_value", models.IntegerField()),
                (
                    "valid_from",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 5, 31, 12, 23, 27, 223876)
                    ),
                ),
                ("valid_to", models.DateTimeField()),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrderCo",
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
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.CharField(default="Không", max_length=255)),
                ("country", models.CharField(default="Việt Nam", max_length=50)),
                (
                    "payment_method",
                    models.CharField(default="Paypal/Credit card", max_length=50),
                ),
                ("order_total", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_at", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders_co",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

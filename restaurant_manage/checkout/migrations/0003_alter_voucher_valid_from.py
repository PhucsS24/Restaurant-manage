# Generated by Django 4.1.2 on 2024-05-31 06:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0002_alter_voucher_valid_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="voucher",
            name="valid_from",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 31, 13, 31, 24, 544685)
            ),
        ),
    ]

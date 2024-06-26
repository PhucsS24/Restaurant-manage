# Generated by Django 4.1.2 on 2024-05-31 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0004_alter_voucher_valid_from"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderco",
            name="delivery_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="orderco",
            name="delivery_time",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="voucher",
            name="valid_from",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 5, 31, 13, 41, 48, 902469)
            ),
        ),
    ]

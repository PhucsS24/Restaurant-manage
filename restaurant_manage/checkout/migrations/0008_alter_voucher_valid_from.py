# Generated by Django 5.0.6 on 2024-05-31 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_voucher_valid_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 18, 51, 41, 674058)),
        ),
    ]

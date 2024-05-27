# Generated by Django 5.0.6 on 2024-05-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '0002_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_location', models.CharField(max_length=100)),
                ('select_size', models.IntegerField()),
                ('choice_date', models.DateField()),
                ('choice_time', models.TimeField()),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('size_party', models.CharField(max_length=100)),
                ('note', models.TextField()),
            ],
        ),
    ]

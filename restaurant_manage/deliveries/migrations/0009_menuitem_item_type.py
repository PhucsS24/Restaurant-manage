# Generated by Django 5.0.3 on 2024-05-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0008_alter_menuitem_price_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='item_type',
            field=models.CharField(choices=[('BEEF', 'Beef'), ('SAUCES', 'Sauces'), ('DESSERT', 'Dessert'), ('DRINK', 'Drink'), ('SOUP', 'Soup'), ('TRADITIONAL', 'Traditional'), ('POPULAR', 'Popular')], default='POPULAR', max_length=20),
        ),
    ]
# Generated by Django 4.0 on 2023-06-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_user_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price_buyer',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='price_seller',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=19),
            preserve_default=False,
        ),
    ]

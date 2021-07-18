# Generated by Django 3.2.4 on 2021-07-08 01:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0007_alter_producto_costo_de_adquisicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costo_de_adquisicion',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]

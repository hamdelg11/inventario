# Generated by Django 3.2.4 on 2021-07-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0005_alter_empleado_apellidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='factura_o_donacion',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='inventario_o_codigo_del_activo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]

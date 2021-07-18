# Generated by Django 3.2.4 on 2021-07-03 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=80)),
                ('apellidoP', models.CharField(max_length=50)),
                ('apellidoM', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('cuenta', models.CharField(max_length=20)),
                ('concepto', models.TextField()),
                ('fecha_adq', models.DateField()),
                ('factura_o_donacion', models.CharField(max_length=20)),
                ('proveedor', models.CharField(max_length=50)),
                ('inventario_o_codigo_del_activo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('marca', models.CharField(max_length=30)),
                ('serie', models.CharField(max_length=50)),
                ('costo_de_adquisicion', models.FloatField()),
                ('clasificacion', models.CharField(max_length=50)),
                ('estado_fisico', models.CharField(choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')], default='B', max_length=1)),
                ('ubicacion', models.CharField(max_length=80)),
                ('observaciones', models.CharField(max_length=150)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inmuebles.empleado')),
            ],
        ),
    ]
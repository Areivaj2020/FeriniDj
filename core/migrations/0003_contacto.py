# Generated by Django 3.1.2 on 2020-11-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aro_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=90)),
                ('apellido', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=254)),
                ('sugerenciaConsulta', models.CharField(max_length=10)),
                ('comunas', models.CharField(max_length=90)),
                ('Mensaje', models.CharField(max_length=300)),
            ],
        ),
    ]

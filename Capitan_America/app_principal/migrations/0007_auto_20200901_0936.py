# Generated by Django 3.1 on 2020-09-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0006_auto_20200901_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hecho',
            name='descripcion_hecho',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Descripción'),
        ),
    ]

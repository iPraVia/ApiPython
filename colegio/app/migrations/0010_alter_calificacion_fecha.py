# Generated by Django 4.1.2 on 2022-12-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_asignatura_id_alter_calificacion_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='fecha',
            field=models.DateField(default=''),
        ),
    ]

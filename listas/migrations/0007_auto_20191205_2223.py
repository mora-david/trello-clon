# Generated by Django 3.0 on 2019-12-05 22:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0006_auto_20191205_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2019, 12, 5, 22, 23, 48, 543194, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lista',
            name='posicion',
            field=models.IntegerField(verbose_name=16548),
        ),
    ]
# Generated by Django 3.0 on 2019-12-05 21:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0002_auto_20191205_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablero',
            name='fecha_de_creacion',
            field=models.DateField(default=datetime.datetime(2019, 12, 5, 21, 36, 27, 488951, tzinfo=utc)),
        ),
    ]

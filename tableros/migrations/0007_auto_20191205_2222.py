# Generated by Django 3.0 on 2019-12-05 22:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0006_auto_20191205_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablero',
            name='fecha_de_creacion',
            field=models.DateField(default=datetime.datetime(2019, 12, 5, 22, 22, 36, 36672, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.0 on 2019-12-09 02:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0016_auto_20191209_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablero',
            name='fecha_de_creacion',
            field=models.DateField(default=datetime.datetime(2019, 12, 9, 2, 35, 12, 872524, tzinfo=utc)),
        ),
    ]
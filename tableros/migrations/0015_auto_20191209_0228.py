# Generated by Django 3.0 on 2019-12-09 02:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0014_auto_20191209_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablero',
            name='fecha_de_creacion',
            field=models.DateField(default=datetime.datetime(2019, 12, 9, 2, 28, 9, 989072, tzinfo=utc)),
        ),
    ]

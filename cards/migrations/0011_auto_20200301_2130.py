# Generated by Django 3.0 on 2020-03-01 21:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_auto_20200301_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2020, 3, 1, 21, 30, 47, 373455, tzinfo=utc)),
        ),
    ]

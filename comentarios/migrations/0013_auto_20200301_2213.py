# Generated by Django 3.0 on 2020-03-01 22:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0012_auto_20200301_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2020, 3, 1, 22, 13, 49, 964329, tzinfo=utc)),
        ),
    ]
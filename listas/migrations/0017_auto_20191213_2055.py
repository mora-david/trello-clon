# Generated by Django 3.0 on 2019-12-13 20:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0016_auto_20191209_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2019, 12, 13, 20, 55, 2, 510492, tzinfo=utc)),
        ),
    ]
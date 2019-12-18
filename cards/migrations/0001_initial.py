# Generated by Django 3.0 on 2019-12-09 01:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listas', '0011_auto_20191209_0156'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(default=datetime.datetime(2019, 12, 9, 1, 56, 16, 387038, tzinfo=utc))),
                ('fecha_vencimiento', models.DateField(null=True)),
                ('posicion', models.IntegerField(null=True)),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tdueño', to=settings.AUTH_USER_MODEL)),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listas.Lista')),
                ('miembros', models.ManyToManyField(related_name='tmiembros', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-30 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0002_endereco'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endereco',
            options={'verbose_name_plural': 'Endereços'},
        ),
        migrations.AddField(
            model_name='endereco',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 20, 1, 23, 854260)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]

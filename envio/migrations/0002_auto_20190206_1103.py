# Generated by Django 2.1.5 on 2019-02-06 10:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nip',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)], verbose_name='NIP UNIZAR'),
        ),
    ]

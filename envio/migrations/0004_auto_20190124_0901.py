# Generated by Django 2.1.5 on 2019-01-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0003_auto_20190123_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='id',
        ),
        migrations.AlterField(
            model_name='centro',
            name='cid',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo de Centro'),
        ),
        migrations.AlterField(
            model_name='centro',
            name='url',
            field=models.URLField(default='http://unizar.es', verbose_name='Página web del centro'),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='eid',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Código de Estudio'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='pid',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Código de Plan'),
        ),
    ]

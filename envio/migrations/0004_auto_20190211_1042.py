# Generated by Django 2.1.5 on 2019-02-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0003_auto_20190208_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrega',
            options={'verbose_name': 'Entrega', 'verbose_name_plural': 'Entregas'},
        ),
        migrations.AlterModelOptions(
            name='matricula',
            options={'verbose_name': 'Matrícula', 'verbose_name_plural': 'Matrículas'},
        ),
        migrations.AlterField(
            model_name='centro',
            name='url',
            field=models.URLField(default='http://unizar.es', verbose_name='Página web del centro'),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='tid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Código de entrega'),
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

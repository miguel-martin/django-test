# Generated by Django 2.1.5 on 2019-02-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0010_entrega_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False, verbose_name='Código del Departamento')),
                ('nombre', models.CharField(max_length=5000)),
            ],
        ),
    ]
# Generated by Django 2.1.5 on 2019-02-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0020_auto_20190215_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='resumen_en',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]

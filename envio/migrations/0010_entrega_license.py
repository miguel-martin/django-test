# Generated by Django 2.1.5 on 2019-02-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0009_remove_entrega_terminos'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrega',
            name='license',
            field=models.IntegerField(choices=[(0, 'No autoriza consulta pública'), (1, 'Autoriza consulta pública')], default=0),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0007_auto_20190213_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='entrega_material_adicional',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='terminos',
            field=models.BooleanField(default=False, help_text='Debes aceptar los Términos y Condiciones para poder realizar la Entrega'),
        ),
    ]
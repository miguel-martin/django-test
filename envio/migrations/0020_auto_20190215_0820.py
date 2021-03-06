# Generated by Django 2.1.5 on 2019-02-15 07:20

from django.db import migrations
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0019_remove_entrega_ficheroprivado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='anexos',
            field=private_storage.fields.PrivateFileField(blank=True, null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='', verbose_name='Anexos'),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='memoria',
            field=private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='', verbose_name='Memoria'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-14 12:46

from django.db import migrations
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0017_auto_20190214_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='ficheroprivado',
            field=private_storage.fields.PrivateFileField(blank=True, null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='', verbose_name='Fichero_privado'),
        ),
    ]

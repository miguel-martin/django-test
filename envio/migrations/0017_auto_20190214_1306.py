# Generated by Django 2.1.5 on 2019-02-14 12:06

from django.db import migrations
import private_files.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0016_auto_20190214_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='anexos2',
        ),
        migrations.AddField(
            model_name='entrega',
            name='ficheroprivado',
            field=private_files.models.fields.PrivateFileField(blank=True, null=True, upload_to='uploads', verbose_name='file'),
        ),
    ]

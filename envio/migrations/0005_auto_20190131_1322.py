# Generated by Django 2.1.5 on 2019-01-31 12:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0004_auto_20190124_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('tid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Código de entrega')),
                ('titulo', models.CharField(max_length=500)),
                ('resumen', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(choices=[('2017', '2017/2018'), ('2018', '2018/2019')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('nip', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(100000)], verbose_name='NIP UNIZAR')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=300)),
                ('email', models.CharField(default='<django.db.models.fields.IntegerField>@unizar.es', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='estudio',
            name='centros',
            field=models.ManyToManyField(through='envio.Plan', to='envio.Centro'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='curso',
            field=models.CharField(choices=[('2017', '2017/2018'), ('2018', '2018/2019')], max_length=4),
        ),
        migrations.AddField(
            model_name='persona',
            name='planes',
            field=models.ManyToManyField(through='envio.Matricula', to='envio.Plan'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envio.Persona'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envio.Plan'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='matricula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envio.Matricula'),
        ),
        migrations.AlterUniqueTogether(
            name='matricula',
            unique_together={('curso', 'persona', 'plan')},
        ),
    ]
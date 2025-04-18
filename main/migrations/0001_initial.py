# Generated by Django 5.1.4 on 2025-01-23 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProducerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer_model', models.CharField(max_length=50, verbose_name='Производитель_и_модель')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время_создания')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_num', models.CharField(max_length=15, verbose_name='Инвентарный номер')),
                ('serial', models.CharField(max_length=20, null=True, verbose_name='Серийный номер')),
                ('building', models.CharField(max_length=10, verbose_name='Корпус')),
                ('location', models.CharField(max_length=50, verbose_name='Расположение')),
                ('note', models.CharField(max_length=250, verbose_name='Примечание')),
                ('hostname', models.CharField(max_length=30, verbose_name='Hostname')),
                ('ip_add', models.CharField(max_length=30, verbose_name='Hostname')),
                ('prod_mod_dev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producermodel')),
            ],
            options={
                'verbose_name': 'Устройство',
                'verbose_name_plural': 'Устройства',
            },
        ),
        migrations.CreateModel(
            name='Cartridges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartridge', models.CharField(max_length=50, verbose_name='Картридж')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Время_создания')),
                ('prod_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producermodel')),
            ],
        ),
    ]

# Generated by Django 5.1.5 on 2025-01-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_num', models.CharField(max_length=15, verbose_name='Инвентарный номер')),
                ('producer', models.CharField(max_length=20, verbose_name='Производитель')),
                ('model', models.CharField(max_length=35, verbose_name='Модель')),
                ('cartridge', models.CharField(max_length=15, verbose_name='Картридж')),
                ('building', models.CharField(max_length=5, verbose_name='Корпус')),
                ('location', models.CharField(max_length=10, verbose_name='Расположение')),
                ('note', models.CharField(max_length=250, verbose_name='Примечание')),
                ('net_address', models.CharField(max_length=30, verbose_name='Hostname/IP')),
            ],
        ),
    ]

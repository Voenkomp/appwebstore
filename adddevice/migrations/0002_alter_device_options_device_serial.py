# Generated by Django 5.1.5 on 2025-01-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adddevice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'Устройство', 'verbose_name_plural': 'Устройства'},
        ),
        migrations.AddField(
            model_name='device',
            name='serial',
            field=models.CharField(max_length=20, null=True, verbose_name='Серийный номер'),
        ),
    ]

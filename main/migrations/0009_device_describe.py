# Generated by Django 5.1.5 on 2025-04-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_device_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='describe',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]

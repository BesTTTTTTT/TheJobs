# Generated by Django 4.2.9 on 2024-02-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_alter_custom_source_alter_custom_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom',
            name='gender',
            field=models.CharField(default='', max_length=255),
        ),
    ]

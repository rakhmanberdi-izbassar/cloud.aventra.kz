# Generated by Django 5.1.7 on 2025-07-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='name_en',
        ),
        migrations.AddField(
            model_name='location',
            name='name_kz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

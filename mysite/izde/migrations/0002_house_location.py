# Generated by Django 5.1.7 on 2025-03-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izde', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='location',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izde', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='category',
        ),
        migrations.AddField(
            model_name='house',
            name='property_type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Villa', 'Villa'), ('Townhouse', 'Townhouse'), ('Penthouse', 'Penthouse'), ('Whole Building', 'Whole Building')], default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

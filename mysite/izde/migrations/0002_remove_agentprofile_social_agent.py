# Generated by Django 5.1.7 on 2025-03-25 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('izde', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentprofile',
            name='social_agent',
        ),
    ]

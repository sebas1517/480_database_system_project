# Generated by Django 4.2.7 on 2023-11-27 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_nurseschedules_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurseschedules',
            name='user',
        ),
    ]
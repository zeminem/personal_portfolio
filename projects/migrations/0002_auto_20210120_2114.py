# Generated by Django 3.1.5 on 2021-01-20 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tehcnology',
            new_name='technology',
        ),
    ]

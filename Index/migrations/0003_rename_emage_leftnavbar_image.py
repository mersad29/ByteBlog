# Generated by Django 5.0.1 on 2024-03-09 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0002_leftnavbar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leftnavbar',
            old_name='emage',
            new_name='image',
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0004_article_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='color',
            field=models.CharField(max_length=20),
        ),
    ]

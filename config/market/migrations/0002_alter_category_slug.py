# Generated by Django 4.1.5 on 2023-01-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='Categorys'),
        ),
    ]

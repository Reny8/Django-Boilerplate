# Generated by Django 4.2.7 on 2023-11-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(choices=[(2, 'PG'), (1, 'G'), (3, 'PG-13'), (4, 'R'), (5, 'NC-17')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.FloatField(),
        ),
    ]

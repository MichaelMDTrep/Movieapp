# Generated by Django 3.1.5 on 2021-01-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0004_auto_20210117_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='movie_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='title',
            field=models.CharField(max_length=350),
        ),
    ]

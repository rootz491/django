# Generated by Django 3.1.3 on 2020-11-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20201119_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.URLField(default='https://images.unsplash.com/photo-1559713044-c7329e177eb0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80', max_length=1000),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist_logo',
            field=models.URLField(default='https://images.unsplash.com/photo-1486092642310-0c4e84309adb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80', max_length=500),
        ),
    ]

# Generated by Django 3.2.6 on 2021-12-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0015_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='blogid',
            field=models.IntegerField(default=0),
        ),
    ]

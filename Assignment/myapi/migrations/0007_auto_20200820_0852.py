# Generated by Django 3.1 on 2020-08-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_auto_20200820_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 3.1.4 on 2021-02-06 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebay', '0006_auto_20210206_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebay',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 17, 7, 42, 142562)),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-05 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0062_auto_20211204_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

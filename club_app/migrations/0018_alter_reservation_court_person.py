# Generated by Django 3.2.8 on 2021-11-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_app', '0017_alter_reservation_court_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Court_Person',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

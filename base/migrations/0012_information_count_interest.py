# Generated by Django 4.0.2 on 2022-02-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='count_interest',
            field=models.FloatField(default=0),
        ),
    ]

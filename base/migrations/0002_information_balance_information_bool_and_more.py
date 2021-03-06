# Generated by Django 4.0.2 on 2022-02-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='information',
            name='bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='information',
            name='interest',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='information',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='information',
            name='dept',
            field=models.IntegerField(default=0),
        ),
    ]

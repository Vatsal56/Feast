# Generated by Django 2.2.5 on 2020-01-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='seats',
            field=models.IntegerField(default=0),
        ),
    ]
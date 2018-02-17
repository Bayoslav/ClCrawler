# Generated by Django 2.0.2 on 2018-02-13 03:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170911_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='name',
            field=models.CharField(default='noname', max_length=100),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 13, 4, 49, 35, 898224)),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='states',
            field=models.CharField(max_length=5000),
        ),
    ]

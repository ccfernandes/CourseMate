# Generated by Django 2.2.3 on 2019-08-22 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20190821_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='review_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 21, 23, 11, 37, 114075), verbose_name='data published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 21, 23, 11, 37, 110146), verbose_name='data published'),
        ),
    ]

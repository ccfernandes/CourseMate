# Generated by Django 2.2.3 on 2019-08-21 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20190821_1027'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 21, 10, 29, 59, 936969), verbose_name='data published'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-07 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroundKeeper', '0007_auto_20190407_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldcondition',
            name='Report_Time_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 18, 56, 35, 263655), help_text='Report Time&Date'),
        ),
    ]
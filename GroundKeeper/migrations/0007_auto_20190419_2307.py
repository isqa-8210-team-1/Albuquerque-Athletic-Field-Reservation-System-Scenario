# Generated by Django 2.1.7 on 2019-04-20 04:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroundKeeper', '0006_auto_20190419_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldcondition',
            name='Report_Time_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 19, 23, 7, 15, 379236), help_text='Report Time&Date'),
        ),
    ]
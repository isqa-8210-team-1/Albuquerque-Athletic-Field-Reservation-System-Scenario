# Generated by Django 2.1.7 on 2019-04-24 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('GroundKeeper', '0013_auto_20190424_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldcondition',
            name='Report_Time_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 21, 1, 43, 78233, tzinfo=utc), help_text='Report Time&Date'),
        ),
    ]

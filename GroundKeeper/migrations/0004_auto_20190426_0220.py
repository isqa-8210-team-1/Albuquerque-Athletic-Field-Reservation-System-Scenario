# Generated by Django 2.1.7 on 2019-04-26 07:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('GroundKeeper', '0003_auto_20190426_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldcondition',
            name='Report_Time_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 7, 20, 41, 56336, tzinfo=utc), help_text='Report Time&Date'),
        ),
    ]

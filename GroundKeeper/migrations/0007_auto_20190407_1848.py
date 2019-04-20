# Generated by Django 2.1.7 on 2019-04-07 23:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkAvail', '0003_delete_fieldcondition'),
        ('GroundKeeper', '0006_auto_20190407_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fieldcondition',
            old_name='name',
            new_name='property_name',
        ),
        migrations.AddField(
            model_name='fieldcondition',
            name='park_name',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, to='parkAvail.Park', verbose_name='park_name'),
        ),
        migrations.AlterField(
            model_name='fieldcondition',
            name='Report_Time_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 18, 48, 17, 954510), help_text='Report Time&Date'),
        ),
    ]

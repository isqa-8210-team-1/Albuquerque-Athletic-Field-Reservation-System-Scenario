# Generated by Django 2.1.7 on 2019-03-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_renter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='First name'),
        ),
    ]

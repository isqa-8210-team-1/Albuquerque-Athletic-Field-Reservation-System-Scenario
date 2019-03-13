# Generated by Django 2.0.5 on 2019-03-07 22:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parkAvail', '0002_auto_20190307_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=100)),
                ('property_description', models.TextField()),
                ('property_guest_capacity', models.IntegerField()),
                ('location_in_park', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('park_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='parkAvail.Park')),
            ],
        ),
    ]
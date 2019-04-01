# Generated by Django 2.1.7 on 2019-03-30 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parkAvail', '0003_delete_fieldcondition'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_number', models.CharField(max_length=50)),
                ('timeslot', models.CharField(blank=True, choices=[('M1', '6.00 A.M to 8.00 A.M'), ('M2', '8.15 A.M to 10.15 A.M'), ('M3', '10.30 A.M to 12.30 P.M'), ('E1', '3.00 P.M to 5.00 P.M'), ('E2', '5.15 P.M to 7.15 P.M')], default='m', max_length=3)),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(default='', max_length=200)),
                ('property_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='parkAvail.Park')),
            ],
        ),
    ]

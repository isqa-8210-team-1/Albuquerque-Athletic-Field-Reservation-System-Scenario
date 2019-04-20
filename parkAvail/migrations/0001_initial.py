# Generated by Django 2.1.7 on 2019-04-20 23:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=50)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('park_address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('park_attendant', models.CharField(blank=True, max_length=50, null=True)),
                ('attendant_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('attendant_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'park',
                'verbose_name_plural': 'parks',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Prop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='props/%Y/%m/%d')),
                ('property_description', models.TextField()),
                ('property_guest_capacity', models.IntegerField()),
                ('location_in_park', models.CharField(blank=True, max_length=50, null=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('park_under', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='props', to='parkAvail.Park')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='prop',
            index_together={('id', 'slug')},
        ),
    ]

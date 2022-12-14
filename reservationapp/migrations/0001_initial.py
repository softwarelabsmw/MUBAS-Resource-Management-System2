# Generated by Django 4.1.1 on 2022-09-18 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=60)),
                ('category', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/resources/')),
                ('availability', models.BooleanField()),
            ],
            options={
                'db_table': 'resource',
                'ordering': ['category', 'resource_name'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(verbose_name='Start Date/Time')),
                ('return_date', models.DateTimeField(verbose_name='Return Date/Time')),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('applying', 'applying'), ('approved', 'approved'), ('declined', 'declined')], default='applying', max_length=9)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservationapp.resource')),
            ],
            options={
                'db_table': 'booking',
                'ordering': ['reservation_date', 'resource_id'],
            },
        ),
    ]

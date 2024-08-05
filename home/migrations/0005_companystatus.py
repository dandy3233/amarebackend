# Generated by Django 5.0.7 on 2024-08-03 11:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_url_herosection_url_driver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('value', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_footerlogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
    ]

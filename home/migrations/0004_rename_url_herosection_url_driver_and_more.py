# Generated by Django 5.0.7 on 2024-08-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_herosection_title_one_herosection_title_two'),
    ]

    operations = [
        migrations.RenameField(
            model_name='herosection',
            old_name='url',
            new_name='url_driver',
        ),
        migrations.AddField(
            model_name='herosection',
            name='url_passanger',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-08 05:58

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CTA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True)),
                ('url_name', models.CharField(max_length=255)),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None)),
                ('image', models.FileField(blank=True, default='cta.jpg', null=True, upload_to='stting')),
            ],
        ),
    ]

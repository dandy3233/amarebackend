# Generated by Django 5.0.7 on 2024-08-04 20:34

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.FileField(blank=True, default='service.jpg', null=True, upload_to='herosection')),
                ('icon', models.FileField(blank=True, default='service.jpg', null=True, upload_to='herosection')),
            ],
        ),
    ]

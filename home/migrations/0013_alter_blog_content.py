# Generated by Django 5.0.7 on 2024-08-04 14:28

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]

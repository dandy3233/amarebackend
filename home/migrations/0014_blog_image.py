# Generated by Django 5.0.7 on 2024-08-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, default='Carddeal.jpg', null=True, upload_to='herosection'),
        ),
    ]

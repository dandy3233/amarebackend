# Generated by Django 5.0.7 on 2024-08-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, default='cta.jpg', null=True, upload_to='stting')),
                ('about_as', models.CharField(max_length=100)),
            ],
        ),
    ]

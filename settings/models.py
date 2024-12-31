from django.db import models
from colorfield.fields import ColorField

# Create your models here.


class CTA(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(max_length=200, blank=True)
    url_name = models.CharField(max_length=255)
    color = ColorField(default='#FF0000')
    image = models.FileField(upload_to="stting", default="cta.jpg", null=True, blank=True)


    def __str__(self):
        return self.title
    
class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to="stting", default="cta.jpg", null=True, blank=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
    
class FooterLogo(models.Model):
    
    logo = models.FileField(upload_to="stting", default="cta.jpg", null=True, blank=True)
    about_as = models.CharField(max_length=100)

class Menu(models.Model):
    
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
class BgColor(models.Model):
    
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.color
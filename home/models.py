from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()  # Use TinyMCE for rich text
    ...


class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    title_one = models.CharField(max_length=200)
    title_two = models.CharField(max_length=200)
    url_passanger = models.URLField(blank=True, null=True)
    url_driver = models.URLField(blank=True, null=True)
    image = models.FileField(upload_to="herosection", default="herosection.jpg", null=True, blank=True)

    def __str__(self):
        return self.title

class CompanyStatus(models.Model):
    title = models.CharField(max_length=100)  # Title or description of the status metric
    value = models.PositiveIntegerField(default=0)  # Numeric value of the status metric
    date = models.DateField(default=timezone.now)  # The date of the status report

    def __str__(self):
        return f"{self.title}: {self.value} on {self.date}"

class FeatureSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    url_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class SiderFeatureSection(models.Model):
    feature_section = models.ForeignKey(FeatureSection, on_delete=models.CASCADE, related_name='sider_features')
    icon = models.FileField(upload_to="herosection", default="featuer.jpg", null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class AppSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to="herosection", default="featuer.jpg", null=True, blank=True)
    iphone_url = models.URLField(blank=True, null=True)
    android_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class CardDeal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(max_length=200, blank=True)
    url_name = models.CharField(max_length=255)

    image = models.FileField(upload_to="herosection", default="Carddeal.jpg", null=True, blank=True)

    
    def __str__(self):
        return self.title

class Blog(models.Model):
    
    title = models.CharField(max_length=255)
    content = HTMLField()
    image = models.FileField(upload_to="herosection", default="Carddeal.jpg", null=True, blank=True)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title
    
class Service(models.Model):
    
    title = models.CharField(max_length=255)
    content = HTMLField()
    image = models.FileField(upload_to="herosection", default="service.jpg", null=True, blank=True)
    icon = models.FileField(upload_to="herosection", default="service.jpg", null=True, blank=True)

    
    def __str__(self):
        return self.title
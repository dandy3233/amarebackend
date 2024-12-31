from rest_framework import serializers
from .models import HeroSection, CompanyStatus, FeatureSection, SiderFeatureSection, AppSection, CardDeal,Blog ,Service

class CardDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDeal
        fields = '__all__'

class AppSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSection
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class CompanyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStatus
        fields = '__all__'


class FeatureSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureSection
        fields = '__all__'

        

class SiderFeatureSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiderFeatureSection
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
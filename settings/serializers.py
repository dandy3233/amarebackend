from rest_framework import serializers
from .models import  CTA, SocialMedia, FooterLogo, Menu, BgColor

class CTASerializer(serializers.ModelSerializer):
    class Meta:
        model = CTA
        fields = '__all__'



class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class FooterLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLogo
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class BgColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BgColor
        fields = '__all__'
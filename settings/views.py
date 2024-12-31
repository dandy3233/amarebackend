from django.shortcuts import render
from rest_framework import generics
from .models import  CTA, SocialMedia, FooterLogo, Menu, BgColor
from .serializers import  CTASerializer, SocialMediaSerializer, FooterLogoSerializer, MenuSerializer, BgColorSerializer

from rest_framework.permissions import AllowAny


class CTAListView(generics.ListAPIView):
    queryset = CTA.objects.all().order_by('-id')[:1]
    serializer_class = CTASerializer
    Permission_class = (AllowAny, )


class SocialMediaViewSet(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    Permission_class = (AllowAny, )

class FooterLogoViewSet(generics.ListAPIView):
    queryset = FooterLogo.objects.all().order_by('-id')[:1]
    serializer_class = FooterLogoSerializer
    Permission_class = (AllowAny, )

class MenuViewSet(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    Permission_class = (AllowAny, )

class BgColorViewSet(generics.ListAPIView):
    queryset = BgColor.objects.all().order_by('-id')[:1]
    serializer_class = BgColorSerializer
    Permission_class = (AllowAny, )
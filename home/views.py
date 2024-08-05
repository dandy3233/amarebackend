from django.shortcuts import render
from rest_framework import generics
from .models import HeroSection, CompanyStatus, FeatureSection, SiderFeatureSection, AppSection, CardDeal, Blog, Service
from .serializers import HeroSectionSerializer, CompanyStatusSerializer, FeatureSectionSerializer, SiderFeatureSectionSerializer, AppSectionSerializer, CardDealSerializer,BlogSerializer, ServiceSerializer
from rest_framework.permissions import AllowAny

class AppSectionListView(generics.ListAPIView):
    queryset = AppSection.objects.all().order_by('-id')[:1]
    serializer_class = AppSectionSerializer
    Permission_class = (AllowAny, )

class HeroSectionList(generics.ListAPIView):
    queryset = HeroSection.objects.all().order_by('-id')[:1]
    serializer_class = HeroSectionSerializer
    Permission_class = (AllowAny, )

class CompanyStatusListView(generics.ListAPIView):
    queryset = CompanyStatus.objects.all().order_by('-id')[:4]
    serializer_class = CompanyStatusSerializer
    Permission_class = (AllowAny, )

class FeatureSectionListView(generics.ListAPIView):
    queryset = FeatureSection.objects.all().order_by('-id')[:1]
    serializer_class = FeatureSectionSerializer
    Permission_class = (AllowAny, )
class SiderFeatureSectionListView(generics.ListAPIView):
    queryset = SiderFeatureSection.objects.all().order_by('-id')[:4]
    serializer_class = SiderFeatureSectionSerializer
    Permission_class = (AllowAny, )
    
class CardDealListView(generics.ListAPIView):
    queryset = CardDeal.objects.all().order_by('-id')[:1]
    serializer_class = CardDealSerializer
    Permission_class = (AllowAny, )

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-id')[:4]
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



class ServiceListView(generics.ListCreateAPIView):
    queryset = Service.objects.all().order_by('-id')[:4]
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
from django.urls import path
from home import views as home_views
from settings import views as stting_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # home
    path('herosection/', home_views.HeroSectionList.as_view()),
    path('company-status/', home_views.CompanyStatusListView.as_view()),
    path('features/', home_views.FeatureSectionListView.as_view()),
    path('side-feature/', home_views.SiderFeatureSectionListView.as_view()),
    path('appsection/', home_views.AppSectionListView.as_view()),
    path('carddeal/', home_views.CardDealListView.as_view()),
    path('blogs/', home_views.BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/',
         home_views.BlogDetailView.as_view(),
         name='blog-detail'),
    path('service/', home_views.ServiceListView.as_view(), name='blog-list'),
    path('service/<int:pk>/',
         home_views.ServiceDetailView.as_view(),
         name='blog-de'),

    # sttings
    path('cta/', stting_views.CTAListView.as_view()),
    path('socialmedia/', stting_views.SocialMediaViewSet.as_view()),
    path('footer-logo/', stting_views.FooterLogoViewSet.as_view()),
    path('menu/', stting_views.MenuViewSet.as_view()),
    path('bgcolor/', stting_views.BgColorViewSet.as_view()),
]

from django.urls import path
from home import views as home_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Other paths auth
    path('herosection/', home_views.HeroSectionList.as_view()),
    path('company-status/', home_views.CompanyStatusListView.as_view()),
    path('features/', home_views.FeatureSectionListView.as_view()),
    path('side-feature/', home_views.SiderFeatureSectionListView.as_view()),
    path('appsection/', home_views.AppSectionListView.as_view()),
    path('carddeal/', home_views.CardDealListView.as_view()),
    path('blogs/', home_views.BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', home_views.BlogDetailView.as_view(), name='blog-detail'),

    path('service/', home_views.ServiceListView.as_view(), name='blog-list'),
    path('service/<int:pk>/', home_views.ServiceDetailView.as_view(), name='blog-de')
]
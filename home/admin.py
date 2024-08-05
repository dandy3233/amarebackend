from django.contrib import admin
from .models import HeroSection, CompanyStatus, FeatureSection, SiderFeatureSection, AppSection, CardDeal,Blog, Service

admin.site.register(HeroSection)

@admin.register(CompanyStatus)
class CompanyStatusAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')
    search_fields = ('title',)
class SiderFeatureSectionInline(admin.TabularInline):
    model = SiderFeatureSection
    extra = 0

class FeatureSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    list_display_links = ('title',)  # Set 'title' as clickable
    list_editable = ()  # Removed 'title' from list_editable since it's already in list_display_links
    search_fields = ('title', 'url_name')
    inlines = [SiderFeatureSectionInline]

    def short_description(self, obj):
        return obj.description[:15] + ('...' if len(obj.description) > 15 else '')
    short_description.short_description = 'Description'

admin.site.register(FeatureSection, FeatureSectionAdmin)

class AppSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    search_fields = ('title',)
    def short_description(self, obj):
        return obj.description[:15] + ('...' if len(obj.description) > 15 else '')
    short_description.short_description = 'Description'

admin.site.register(AppSection, AppSectionAdmin)


@admin.register(CardDeal)
class CardDealAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date','image')
    search_fields = ('title', 'author__username')
  
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
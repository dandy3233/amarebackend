from django.contrib import admin
from .models import CTA, SocialMedia, FooterLogo, Menu, BgColor
from django.utils.html import format_html
# Register your models here.

class CTAAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    search_fields = ('title',)
    def short_description(self, obj):
        return obj.description[:15] + ('...' if len(obj.description) > 15 else '')
    short_description.short_description = 'Description'

admin.site.register(CTA, CTAAdmin)




class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_display', 'url')
    search_fields = ('name',)

    def icon_display(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="50" height="50" />', obj.icon.url)
        return '-'

    icon_display.short_description = 'Icon'

admin.site.register(SocialMedia, SocialMediaAdmin)



class FooterLogoAdmin(admin.ModelAdmin):
    list_display = ('about_as_display', 'icon_display')

    def about_as_display(self, obj):
        # Limit the description to 10 words
        description = obj.about_as
        words = description.split()
        if len(words) > 10:
            return ' '.join(words[:10]) + '...'
        return description

    def icon_display(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return '-'

    about_as_display.short_description = 'Description'
    icon_display.short_description = 'Logo'

admin.site.register(FooterLogo, FooterLogoAdmin)

admin.site.register(Menu)


class BgColorAdmin(admin.ModelAdmin):
    # Display the color as a preview in the list view
    def color_display(self, obj):
        return format_html(
            '<div style="width: 50px; height: 20px; background-color: {};"></div>',
            obj.color
        )

    color_display.short_description = 'Color Preview'

    list_display = ('color_display',)

    # Customize the form widget to show a color preview
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'color':
            kwargs['widget'] = admin.widgets.AdminTextInputWidget()
        return super().formfield_for_dbfield(db_field, request, **kwargs)

admin.site.register(BgColor, BgColorAdmin)



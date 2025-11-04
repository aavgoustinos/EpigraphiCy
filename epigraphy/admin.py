from django.contrib import admin
from django.utils.html import format_html
from .models import Epigraphy,Monument,IconographicElement


admin.site.register(Monument)
admin.site.register(IconographicElement)


class EpigraphyAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_1_tag','id')  # Add the method for displaying image_1
    
    def image_1_tag(self, obj):
        if obj.image_1:
            return format_html('<img src="{}" width="100" height="100" />', obj.image_1.url)
        return "No Image"
    
    image_1_tag.short_description = 'Image 1 Preview'

admin.site.register(Epigraphy, EpigraphyAdmin)
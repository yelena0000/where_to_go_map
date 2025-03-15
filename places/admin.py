from django.contrib import admin
from django.utils.html import format_html
from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ['image', 'image_preview', 'order',]
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px;" />',
                obj.image.url
            )
        return "(No image)"

    image_preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ('title',)


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'image', 'order')
    ordering = ['place', 'order']

from django import forms
from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from tinymce.widgets import TinyMCE

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ['image', 'image_preview', 'order', 'place']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px;" />',
                obj.image.url
            )
        return '(No image)'

    image_preview.short_description = 'Превью'


class PlaceAdminForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
        widgets = {
            'long_description': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    form = PlaceAdminForm
    inlines = [PlaceImageInline]
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('place', 'order', 'image_preview', 'image')
    list_filter = ('place',)
    search_fields = ('place__title',)
    raw_id_fields = ('place',)
    autocomplete_fields = ('place',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px;" />',
                obj.image.url
            )
        return '(No image)'

    image_preview.short_description = 'Превью'

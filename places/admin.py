from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from tinymce.widgets import TinyMCE
from .models import Place, PlaceImage
from django import forms


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ['image', 'image_preview', 'order',]
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px;" />', obj.image.url)
        return "(No image)"

    image_preview.short_description = "Превью"


class PlaceAdminForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

    description_long = forms.CharField(
        widget=TinyMCE(attrs={'cols': 80, 'rows': 30})
    )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    form = PlaceAdminForm
    inlines = [PlaceImageInline]
    list_display = ('title',)
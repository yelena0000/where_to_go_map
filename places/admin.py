from django.contrib import admin
from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ['image', 'order',]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ('title',)


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'image', 'order')
    ordering = ['place', 'order']

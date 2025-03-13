from django.contrib import admin
from .models import Place, PlaceImage

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'image', 'order')
    ordering = ['place', 'order']

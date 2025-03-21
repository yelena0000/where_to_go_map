from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        unique=True
    )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True
    )
    long_description = HTMLField(
        verbose_name='Полное описание',
        blank=True
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Локация'
    )
    image = models.ImageField(
        upload_to='places_images/',
        verbose_name='Изображение',
        blank=True,
        null=True
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name='Порядок'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['order']

    def __str__(self):
        return f'{self.order} - {self.place.title}'

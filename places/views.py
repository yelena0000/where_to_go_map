from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Prefetch

from .models import Place, PlaceImage


def index(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude],
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_detail', args=[place.id]),
            },
        })

    geojson = {
        'type': 'FeatureCollection',
        'features': features,
    }

    return render(request, 'index.html', {'geojson': geojson})


def get_place_details(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related(
            Prefetch('images', queryset=PlaceImage.objects.all())
        ),
        id=place_id
    )

    imgs = [image.image.url for image in place.images.all()]

    place_content = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'latitude': place.latitude,
        'longitude': place.longitude,
    }

    return JsonResponse(place_content, json_dumps_params={'ensure_ascii': False, 'indent': 4})

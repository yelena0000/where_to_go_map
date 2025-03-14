from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place

def index(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude],
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"/places/{place.id}/",
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, 'index.html', {'geojson': geojson})


def get_place_details(request, place_id):

    place = get_object_or_404(Place, id=place_id)
    images = place.images.all()
    imgs = [image.image.url for image in images]

    data = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'latitude': place.latitude,
        'longitude': place.longitude,
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})


from django.shortcuts import render
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
                "detailsUrl": "/places/detail_placeholder/" ,
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, 'index.html', {'geojson': geojson})


import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Загружает данные о месте из JSON по указанному URL"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="URL JSON-файла с описанием места")

    def handle(self, *args, **kwargs):
        url = kwargs["url"]
        self.stdout.write(f"Загружаю данные из {url}...")

        try:
            response = requests.get(url)
            response.raise_for_status()
            place_content = response.json()
        except requests.RequestException as error:
            self.stderr.write(f"Ошибка загрузки JSON: {error}")
            return

        title = place_content["title"]
        place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                "description_short": place_content.get("description_short", ""),
                "description_long": place_content.get("description_long", ""),
                "latitude": float(place_content["coordinates"]["lat"]),
                "longitude": float(place_content["coordinates"]["lng"]),
            },
        )

        for order, image_url in enumerate(place_content["imgs"], start=1):
            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                image_name = image_url.split("/")[-1]

                place_image = PlaceImage(
                    place=place,
                    order=order
                )
                place_image.image.save(
                    image_name,
                    ContentFile(image_response.content),
                    save=True
                )

                self.stdout.write(f"Загружено изображение ({order}): {image_name}")
            except requests.RequestException as error:
                self.stderr.write(f"Ошибка загрузки изображения {image_url}: {error}")

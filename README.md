# Куда пойти — Москва
## Описание проекта
Проект представляет собой сайт, на котором отображаются различные локации Москвы с возможностью их просмотра и редактирования через админку.


Сайт доступен по [ссылке.](https://yelena0000.pythonanywhere.com/)

## Как запустить сайт локально

### 1. Скачайте или клонируйте репозиторий:

```shell
git clone https://github.com/yelena0000/where_to_go_map.git
```

### 2. Установите зависимости:

```shell
pip install -r requirements.txt
```

Рекомендуется использовать виртуальное окружение.

### 3. Настройте переменные окружения:

Создайте файл `.env` в корне проекта и добавьте в него следующие переменные:


```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Применените миграции и запустите сервер:

```shell
python manage.py migrate
python manage.py runserver
```
Перейдите по адресу: http://127.0.0.1:8000/

### 5. Доступ к админке:

Перейдите по адресу http://127.0.0.1:8000/admin/

Создайте суперпользователя, если его ещё нет:

```shell
python manage.py createsuperuser
```

## Добавление и редактирование локаций:

Чтобы добавить данные, выполните следующие шаги:

### 1. Перейдите в админку по адресу:
http://127.0.0.1:8000/admin/

Войдите, используя логин и пароль суперпользователя.

### 2. В админке откройте раздел **"Локации"**.

Нажмите **"Добавить"** и заполните следующие поля:

- Название локации.
- Краткое описание.
- Полное описание.
- Координаты (широта и долгота).
- Фотографии (загрузите изображения).

Сохраните локацию и убедитесь, что она корректно отображается на сайте.



## Работа с медиа-файлами

Все изображения загружаются в директорию `media/places_images/`.

При разработке медиа-файлы доступны по адресу `/media/`.

### Настройка в `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'
```
### Для локальной раздачи медиа в `urls.py` добавьте:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

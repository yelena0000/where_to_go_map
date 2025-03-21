# Куда пойти — Москва
## Описание проекта
Проект представляет собой сайт, на котором отображаются различные локации Москвы с возможностью их просмотра и редактирования через админку.


Сайт доступен по [ссылке.](https://yelena0000.pythonanywhere.com/)

## Как запустить сайт локально

Проект работает на `Python` версии `3.10`. Вы можете проверить свою версию командой:

```shell
python --version
```
Если у вас установлена подходящая версия `Python`, можете переходить к следующим шагам.
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

`SECRET_KEY`

**Назначение:** Используется для криптографической подписи, важен для безопасности сессий и данных, связанных с cookies.

**Примечание:** Никогда не размещайте SECRET_KEY в публично доступных источниках.

`DEBUG`

**Назначение:** При включении выводит подробную информацию об ошибках, что может быть опасно на продакшн сервере.

**Примечание:** Всегда устанавливайте `DEBUG = False` на продакшн серверах.

`ALLOWED_HOSTS`

**Назначение:** Определяет список строк, представляющих имена хостов/доменов, которым разрешено обслуживать этот сайт.

**Примечание:** Настройте это значение в соответствии с доменами, на которых должно работать ваше приложение.


Более подробно с назначением этих переменных можно ознакомиться в документации Django: [SECRET_KEY](https://docs.djangoproject.com/en/5.1/ref/settings/#secret-key), [DEBUG](https://docs.djangoproject.com/en/5.1/ref/settings/#debug), [ALLOWED_HOSTS](https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts).

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

### 1. Через админку:

Перейдите в админку по адресу:
http://127.0.0.1:8000/admin/

Войдите, используя логин и пароль суперпользователя.

В админке откройте раздел **"Локации"**, нажмите **"Добавить"** и заполните следующие поля:

- Название локации.
- Краткое описание.
- Полное описание.
- Координаты (широта и долгота).
- Фотографии (загрузите изображения).

Сохраните локацию и убедитесь, что она корректно отображается на сайте.

### 2. Через команду `load_place`:

Вы можете автоматически загружать данные о локациях из JSON-файлов по URL.

Для этого используйте команду:

```shell
python manage.py load_place http://адрес/файла.json
```

### Пример содержимого JSON-файла:
```
{
    "title": "Красная площадь",
    "imgs": [
        "http://example.com/krasnaya1.jpg",
        "http://example.com/krasnaya2.jpg"
    ],
    "description_short": "Главная площадь Москвы",
    "description_long": "<p>Красная площадь — это сердце столицы...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.621391
    }
}
```

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

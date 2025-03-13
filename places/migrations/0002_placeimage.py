# Generated by Django 4.2 on 2025-03-13 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='places_images/', verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Локация')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]

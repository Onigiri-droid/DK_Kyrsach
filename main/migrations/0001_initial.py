# Generated by Django 5.0.4 on 2024-04-23 19:51

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('mail', models.EmailField(max_length=254, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('programs_start', models.DateTimeField(verbose_name='Начало программы')),
                ('programs_end', models.DateTimeField(verbose_name='Конец программы')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='competition_images/', verbose_name='Изображение')),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True)),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.contacts', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Соревнование',
                'verbose_name_plural': 'Соревнования',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('start', models.DateTimeField(verbose_name='Дата начала')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='news_images/', verbose_name='Изображение')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('competition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='main.competition', verbose_name='Соревнование')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.contacts', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(verbose_name='Рейтинг')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.competition', verbose_name='Соревнование')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
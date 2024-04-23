from django.db import models
from autoslug import AutoSlugField


class Competition(models.Model):
    title = models.CharField('Название', max_length=100)
    programs_start = models.DateTimeField('Начало программы')
    programs_end = models.DateTimeField('Конец программы')
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='competition_images/')
    contacts = models.ForeignKey('Contacts', verbose_name="Контакты", on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, db_index=True, always_update=True)


    def __str__(self):
        return f'{self.title} - {self.programs_start} - {self.programs_end} - {self.slug}'

    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"


class Review(models.Model):
    competition = models.ForeignKey(Competition, verbose_name="Соревнование", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField('Рейтинг')
    comment = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.competition.title} - {self.rating}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class News(models.Model):
    title = models.CharField('Название', max_length=100)
    start = models.DateTimeField('Дата начала')
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='news_images/')
    competition = models.ForeignKey(Competition, verbose_name="Соревнование", on_delete=models.CASCADE,
                                    related_name='news', blank=True, null=True)
    contacts = models.ForeignKey('Contacts', verbose_name="Контакты", on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return f'{self.start} - {self.description}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Contacts(models.Model):
    address = models.CharField('Адрес', max_length=100, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=20)
    mail = models.EmailField('Почта')

    def __str__(self):
        return f'{self.address} - {self.phone}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

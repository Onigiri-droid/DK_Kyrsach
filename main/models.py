from django.db import models
from autoslug import AutoSlugField


class Competition(models.Model):
    title = models.CharField('Название', max_length=100)
    programs_start = models.DateTimeField('Начало программы')
    programs_end = models.DateTimeField('Конец программы')
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='competition_images/')
    contacts = models.ForeignKey('Contacts', verbose_name="Контакты", on_delete=models.CASCADE)
    age = models.ForeignKey('Age', verbose_name="Возраст", on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, db_index=True, always_update=True)

    def __str__(self):
        return f'{self.title} - {self.programs_start} - {self.programs_end} - {self.slug}'

    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"


class News(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='news_images/')
    contacts = models.ForeignKey('Contacts', verbose_name="Контакты", on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Contacts(models.Model):
    address = models.CharField('Адрес', max_length=100, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=20)
    mail = models.EmailField('Почта')

    def __str__(self):
        return f'{self.address} - {self.phone} - {self.mail}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Lesson(models.Model):
    title = models.CharField('Название', max_length=100)
    age = models.ForeignKey('Age', verbose_name="Возраст участника", on_delete=models.CASCADE)
    having_place = models.ForeignKey('Having', verbose_name="Длительность занятия", on_delete=models.CASCADE)
    duration_lesson = models.ForeignKey('Time', verbose_name="Наличие мест", on_delete=models.CASCADE)
    cost_lesson = models.CharField('Стоимость', max_length=100)
    repetitions_week = models.CharField('Занятий в неделю', max_length=100)
    duration_training = models.CharField('Длительность обучения', max_length=100)
    description = models.TextField('Описание')
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, db_index=True, always_update=True)

    def __str__(self):
        return f'{self.title} - {self.age} - {self.having_place} - {self.duration_lesson}'

    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"


class Review(models.Model):
    rating = models.PositiveSmallIntegerField('Рейтинг')
    comment = models.TextField('Комментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    lesson = models.ManyToManyField('Lesson', related_name='Review')

    def __str__(self):
        return f'{self.comment} - {self.rating}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Age(models.Model):
    participants = models.CharField('Возраст', max_length=50)

    def __str__(self):
        return f'{self.participants}'

    class Meta:
        verbose_name = "Врзраст участника"
        verbose_name_plural = "Возраст участников"


class Having(models.Model):
    place = models.CharField('Наличие', max_length=50)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        verbose_name = "Наличие мест"
        verbose_name_plural = "Наличие мест"


class Time(models.Model):
    duration = models.CharField('Длительность', max_length=50)

    def __str__(self):
        return f'{self.duration}'

    class Meta:
        verbose_name = "Длительность занятия"
        verbose_name_plural = "Длительность занятия"

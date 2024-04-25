from django.shortcuts import render
from .models import *

def index(request):
    # tasks = Competition.objects.order_by('-id')[:3]
    # context = {
    #     'form': form,
    #     'error': error
    # }
    return render(request, 'main/index.html')



# урок_1 = Урок.objects.create(название='Математика')
# отзыв_1 = Отзыв.objects.create(текст='Отличный урок!')
# отзыв_2 = Отзыв.objects.create(текст='Прекрасный курс!')
#
# # Добавляем связи между уроками и отзывами
# урок_1.отзывы.add(отзыв_1, отзыв_2)
#
# # Получаем все отзывы для конкретного урока
# отзыви_урока_1 = урок_1.отзывы.all()
#
# # Получаем все уроки для конкретного отзыва
# уроки_отзыва_1 = отзыв_1.уроки.all()
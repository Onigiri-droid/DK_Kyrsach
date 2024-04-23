from django.shortcuts import render
from .models import *

def index(request):
    # tasks = Competition.objects.order_by('-id')[:3]
    # context = {
    #     'form': form,
    #     'error': error
    # }
    return render(request, 'main/index.html')

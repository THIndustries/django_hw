from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Главная страница посещена')
    return render(request, 'home.html')

def about(request):
    logger.info('Страница обо мне посещена')
    return render(request, 'about.html')
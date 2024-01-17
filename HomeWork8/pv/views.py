import random

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from datetime import datetime
from time import time, localtime, strftime


# Create your views here.


def index(request):
    return render(request, 'pv/templates/home.html')


def home(request):
    return render(request, 'pv/templates/home.html')


def news(request):
    return render(request, 'pv/templates/news.html')


def boss(request):
    return render(request, 'pv/templates/boss.html')


def facts(request):
    # leader_name = request.GET.get("name", None)
    # if leader_name is None:
    #     return HttpResponseRedirect('news')
    # return render(request, 'pv/templates/facts.html', context={"info": leader_name})
    return render(request, 'pv/templates/facts.html')


def contacts(request):
    return render(request, 'pv/templates/contacts.html')


# Обработчик неправильных адресов
def invalid_address(request):
    return render(request, 'pv/templates/news.html')

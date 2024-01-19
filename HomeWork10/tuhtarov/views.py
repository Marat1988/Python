from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'tuhtarov/templates/index.html')


def task1(request):
    return render(request, 'tuhtarov/templates/task1.html')

from django.shortcuts import render
import locale
from datetime import datetime
from babel.dates import format_date

# устанавливаем русскую локаль
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


# Create your views here.

def task1(request):
    if request.method == 'POST':
        number1 = int(request.POST['number1'])
        number2 = int(request.POST['number2'])
        number3 = int(request.POST['number3'])
        result = {"Максимальное значение ": max(number1, number2, number3),
                  "Минимальное значение ": min(number1, number2, number3),
                  "Среднее значение ": (number1 + number2 + number3)/3.0}
        return render(request, 'tuhtarov/templates/task1.html', {'result': result})
    return render(request, 'tuhtarov/templates/task1.html')


def index(request):
    return render(request, 'tuhtarov/templates/index.html')

#https://babel.pocoo.org/en/latest/api/dates.html
def task2(request):
    if request.method == 'POST':
        year = int(request.POST['year'])
        programmer_date = datetime(year, 9, 13)
        formatted_date = format_date(programmer_date, format='d MMMM (EEEE)', locale='ru_RU')
        return render(request, 'tuhtarov/templates/task2.html', {'programmer_date': formatted_date})
    return render(request, 'tuhtarov/templates/task2.html')

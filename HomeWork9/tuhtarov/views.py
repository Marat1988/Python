from django.shortcuts import render
from tuhtarov.models import Order


# Create your views here.


def index(request):
    return render(request, 'tuhtarov/templates/order.html')


def order(request):
    order_user = request.POST
    if order_user:
        order_new = Order.objects.create(firstname=order_user['firstname'], lastname=order_user['lastname'], phone=order_user['phone'], address=order_user['address'], monthCount=order_user['monthCount'], capacity=order_user['capacity'])
        order_new.save()
    return render(request,
                  "tuhtarov/templates/order.html", {'order': order_user})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from tuhtarov.models import Restaurant


# Create your views here.

def index(request):
    return render(request, 'tuhtarov/templates/main.html')


def add(request):
    restaurant = request.POST
    if restaurant:
        restaurant_new = Restaurant.objects.create(name=restaurant['name'], specialization=restaurant['specialization'],
                                                   address=restaurant['address'],
                                                   site=restaurant['site'], telephone=restaurant['telephone'])
        restaurant_new.save()
    return render(request, 'tuhtarov/templates/add.html', context={"restaurant": restaurant})


def invalid_address(request):
    return render(request, 'tuhtarov/templates/main.html')


def all(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'tuhtarov/templates/all.html', context={"all_restaurants": all_restaurants})


def delete(request, id):
    try:
        delete_restaurant = Restaurant.objects.get(id=id)
        delete_restaurant.delete()
    except:
        pass
    return HttpResponseRedirect(redirect_to="/all/")


def edit(request, id):
    try:
        restaurant = Restaurant.objects.get(id=id)
        return render(request, "tuhtarov/templates/restaurant_edit.html", context={"restaurant": restaurant})
    except:
        return HttpResponseRedirect(redirect_to="/all/")


def change_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)
    print(restaurant.specialization)
    restaurant.name = request.POST.get("name", "")
    restaurant.specialization = request.POST.get("specialization", "")
    restaurant.address = request.POST.get("address", "")
    restaurant.site = request.POST.get("site", "")
    restaurant.telephone = request.POST.get("telephone", "")
    restaurant.save()
    return HttpResponseRedirect(redirect_to="/all/")


def find(request):
    specialization = request.GET.get("specialization")
    restaurants = Restaurant.objects.filter(specialization=specialization).order_by("name")
    return render(request, 'tuhtarov/templates/find.html',context={"restaurants": restaurants})


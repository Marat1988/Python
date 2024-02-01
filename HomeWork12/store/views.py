from datetime import date, datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from store.models import Seller, Buyer, Product, SoldInfo


def index(request):
    return render(request, "store/templates/index.html")


def store_info(request):
    if request.method == "POST":
        try:
            buyer_new = Buyer.objects.get(id=int(request.POST.get("buyer")))
            seller_new = Seller.objects.get(id=int(request.POST.get("seller")))
            product_new = Product.objects.get(id=int(request.POST.get("product")))
            sold_new = SoldInfo(buyer=buyer_new,
                                seller=seller_new,
                                product=product_new,
                                sold_price=float(request.POST.get("price")),
                                product_amount=int(request.POST.get("product_amount")),
                                sold_date=date.today())
            sold_new.save()
        except Exception as e:
            print(e)
    sold_info = SoldInfo.objects.all()
    all_buyers = Buyer.objects.all()
    all_sellers = Seller.objects.all()
    all_products = Product.objects.all()
    return render(
        request,
        "store/templates/store-info.html",
        context={"sold_info": sold_info,
                 "all_buyers": all_buyers,
                 "all_sellers": all_sellers,
                 "all_products": all_products}
    )


def seller_info(request):
    seller = request.POST
    if seller:
        try:
            seller_new = Seller.objects.create(firstname=seller['firstname'], lastname=seller['lastname'],
                                               phone=seller['phone'], email=seller['email'],
                                               start_date=seller['start_date'],
                                               vacancy=seller['vacancy'])
            seller_new.save()
        except:
            pass
    sellers = Seller.objects.all()
    return render(request,
                  "store/templates/seller-info.html",
                  context={"seller_info": sellers})


def del_seller(request, id):
    try:
        delete_seller = Seller.objects.get(id=id)
        delete_seller.delete()
    except:
        pass
    return HttpResponseRedirect(redirect_to="/seller-info/")


def edit_seller(request, id):
    try:
        seller = Seller.objects.get(id=id)
        seller.start_date = datetime.strftime(seller.start_date, "%Y-%m-%d")
        return render(request, "store/templates/seller_edit.html", context={"seller": seller})
    except:
        return HttpResponseRedirect(redirect_to="/seller-info/")


def change_seller(request, id):
    try:
        seller = Seller.objects.get(id=id)
        seller.firstname = request.POST.get("firstname", "")
        seller.lastname = request.POST.get("lastname", "")
        seller.phone = request.POST.get("phone", "")
        seller.email = request.POST.get("email", "")
        seller.start_date = request.POST.get('start_date')
        seller.vacancy = request.POST.get("vacancy", "")
        seller.save()
    except Exception as a:
        print(a)
    return HttpResponseRedirect(redirect_to="/seller-info/")


# -------------------------------------------------------------------------#
def buyer_info(request):
    buyer = request.POST
    if buyer:
        try:
            buyer_new = Buyer.objects.create(firstname=buyer['firstname'], lastname=buyer['lastname'],
                                             phone=buyer['phone'], email=buyer['email'])
            buyer_new.save()
        except:
            pass
    buyers = Buyer.objects.all()
    return render(request,
                  "store/templates/buyer-info.html",
                  context={"buyer_info": buyers})


def del_buyer(request, id):
    try:
        delete_buyer = Buyer.objects.get(id=id)
        delete_buyer.delete()
    except:
        pass
    return HttpResponseRedirect(redirect_to="/buyer-info/")


def edit_buyer(request, id):
    try:
        buyer = Buyer.objects.get(id=id)
        return render(request, "store/templates/buyer_edit.html", context={"buyer": buyer})
    except:
        return HttpResponseRedirect(redirect_to="/buyer-info/")


def change_buyer(request, id):
    try:
        buyer = Buyer.objects.get(id=id)
        buyer.firstname = request.POST.get("firstname", "")
        buyer.lastname = request.POST.get("lastname", "")
        buyer.phone = request.POST.get("phone", "")
        buyer.email = request.POST.get("email", "")
        buyer.save()
    except Exception as a:
        print(a)
    return HttpResponseRedirect(redirect_to="/buyer-info/")


# -------------------------------------------------------------------------#

def product_info(request):
    product = request.POST
    if product:
        try:
            product_new = Product.objects.create(name=product["name"],
                                                 description=product["description"],
                                                 price=product["price"],
                                                 storage_amount=product["storage_amount"])
            product_new.save()
        except:
            pass
    products = Product.objects.all()
    return render(request,
                  "store/templates/product-info.html",
                  context={"product_info": products})


def del_product(request, id):
    try:
        delete_product = Product.objects.get(id=id)
        delete_product.delete()
    except:
        pass
    return HttpResponseRedirect(redirect_to="/product-info/")


def edit_product(request, id):
    try:
        product = Product.objects.get(id=id)
        return render(request, "store/templates/product_edit.html", context={"product": product})
    except:
        return HttpResponseRedirect(redirect_to="/product-info/")


def change_product(request, id):
    try:
        product = Product.objects.get(id=id)
        product.name = request.POST.get("name", "")
        product.description = request.POST.get("description", "")
        product.price = request.POST.get("price", "")
        product.storage_amount = request.POST.get("storage_amount", "")
        product.save()
    except Exception as a:
        print(a)
    return HttpResponseRedirect(redirect_to="/product-info/")

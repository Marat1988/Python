"""
URL configuration for best_store_pv_113 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('del_seller/<int:id>', views.del_seller, name="del_seller"),
    path('change_seller/<int:id>', views.change_seller, name="change_seller"),
    re_path(r'^seller-info/?$', views.seller_info, name="seller-info"),
    path('edit_seller/<int:id>', views.edit_seller, name="edit_seller"),

    path('del_buyer/<int:id>', views.del_buyer, name="del_buyer"),
    path('change_buyer/<int:id>', views.change_buyer, name="change_buyer"),
    re_path(r'^buyer-info/?$', views.buyer_info, name="buyer-info"),
    path('edit_buyer/<int:id>', views.edit_buyer, name="edit_buyer"),





    re_path(r'^store-info/?$', views.store_info, name="store-info"),

]

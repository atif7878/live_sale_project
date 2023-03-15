from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def store(request):
     categorys = Category.objects.all()
     context = {'categorys': categorys}
     return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_item = order.get_cart_items
    else:
        items = []
        cart_item = 0
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'cart_item': cart_item}
    return render(request, 'store/cart.html', context)


def checkout(request):
      if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cart_item = order.get_cart_items
      else:
            items = []
            cart_item = 0
            order = {'get_cart_total': 0, 'get_cart_items': 0}
      context = {'items': items, 'cart_item': cart_item}
      return render(request, 'store/checkout.html', context)


def categorys(request):
      categorysitem = CategoryItem.objects.all()
      context = {'categorysitem' : categorysitem}
      return render(request, 'store/category.html', context)


def categroy_detail(request, pk):
      categorysitem = get_object_or_404(CategoryItem, pk=pk)
      context = {'categorysitem' : categorysitem}
      return render(request, 'store/categroy_detail.html', context)
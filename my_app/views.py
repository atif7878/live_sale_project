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
            Order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = Order.orderitem_set.all()
      else:
            items = []
      context = {'items':items}
      return render(request, 'store/cart.html', context)


def checkout(request):
      context = {}
      return render(request, 'store/checkout.html', context)


def categorys(request):
      categorysitem = CategoryItem.objects.all()
      context = {'categorysitem' : categorysitem}
      return render(request, 'store/category.html', context)


def categroy_detail(request, pk):
      categorysitem = get_object_or_404(CategoryItem, pk=pk)
      context = {'categorysitem' : categorysitem}
      return render(request, 'store/categroy_detail.html', context)
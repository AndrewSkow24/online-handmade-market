from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product, Category, Contact


def product_list(request):
    products = Product.objects.all()
    context = {
        "title": "Список всех товаров",
        "products": products,
    }
    return render(request, "catalog/product_list.html", context=context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    print(product)
    context = {
        "title": "Подробнее о ...",
        "product": product,
    }
    return render(request, "catalog/product_detail.html", context=context)


class ContactList(ListView):
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"


def send_us(request):
    return render(request, "catalog/send_us.html")

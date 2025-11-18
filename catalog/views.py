from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from .models import Contact


def index(request):
    print("Просто ради забавы в консоль")
    product_list = Product.objects.all()
    for product_item in product_list[:5]:
        print(product_item.__dict__)

    return render(request, "catalog/index.html")


class ContactList(ListView):
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"


def send_us(request):
    return render(request, "catalog/send_us.html")

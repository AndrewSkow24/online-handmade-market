from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .models import Product, Contact


class ProductCreateView(CreateView):
    model = Product
    fields = (
        "name",
        "description",
        "image",
        "category",
        "price",
    )
    success_url = reverse_lazy("catalog:product_list")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = (
        "name",
        "description",
        "image",
        "category",
        "price",
    )
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactList(ListView):
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"


def send_us(request):
    return render(request, "catalog/send_us.html")

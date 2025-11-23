from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .models import Product, Contact, Version
from .forms import ProductForm, VersionForm
from django.forms import inlineformset_factory


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactList(ListView):
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"


def send_us(request):
    return render(request, "catalog/send_us.html")

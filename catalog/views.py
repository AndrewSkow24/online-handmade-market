from pyexpat.errors import messages

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .models import Product, Contact, Version
from .forms import ProductForm, VersionForm, ProductModerForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("users:login")

    def form_valid(self, form):
        product = form.save()
        # автоматическая привязка пользователя при создании
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all().order_by("-updated_at")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = reverse_lazy("users:login")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("users:login")

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

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm
        if (
            user.has_perm("catalog.can_cancel_publish")
            and user.has_perm("catalog.can_change_category")
            and user.has_perm("catalog.can_change_description")
        ):
            return ProductModerForm
        else:
            raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    login_url = reverse_lazy("users:login")


class ContactList(ListView):
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"


def send_us(request):
    return render(request, "catalog/send_us.html")

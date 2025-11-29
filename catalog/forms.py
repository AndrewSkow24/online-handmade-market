from django import forms
from .models import Product, Version
from django.forms import BooleanField


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["owner"]


class ProductModerForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # может отменять публикацию продукта,
        # может менять описание любого продукта,
        # может менять категорию любого продукта.
        fields = ["is_published", "description", "category"]

    def clean_name(self):
        cleaned_name = self.cleaned_data.get("name")

        for forbidden_word in forbidden_words:
            if forbidden_word.lower() in cleaned_name.lower():
                raise forms.ValidationError(
                    f'Нельзя использовать "{forbidden_word}" в названии товара'
                )

        return cleaned_name


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

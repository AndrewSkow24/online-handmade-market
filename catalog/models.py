from django.db import models

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="products/", verbose_name="Изображение", **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="категория",
        related_name="products",
    )
    price = models.FloatField(verbose_name="цена за покупку")
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Version(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    version_num = models.PositiveSmallIntegerField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=64, verbose_name="Название версии")
    is_actual = models.BooleanField(default=False, verbose_name="Текущая версия")


class Contact(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=255, verbose_name="Телефон")
    email = models.EmailField(max_length=255, verbose_name="Электронная почта")
    about_me = models.TextField(verbose_name="Информация о себе")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

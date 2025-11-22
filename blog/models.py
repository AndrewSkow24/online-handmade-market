from django.db import models
from catalog.models import NULLABLE


class Post(models.Model):
    """
    Модель записи блога
    """

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, verbose_name="slug")
    body = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog/", verbose_name="Изображение", **NULLABLE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Последнее обновление"
    )
    is_published = models.BooleanField(default=True, verbose_name="Признак публикации")
    counter_views = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров", default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"

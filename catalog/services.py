# сервисная функция,
# которая будет отвечать за выборку категорий
# и которую можно переиспользовать в любом месте системы


from django.core.cache import cache
from catalog.models import Product


def get_products_by_category(category_pk):
    cache_key = f"category_list_{category_pk}"
    products = cache.get(cache_key)
    if not products:
        products = Product.objects.filter(category_id=category_pk)
        cache.set(cache_key, products, 60)
    return products

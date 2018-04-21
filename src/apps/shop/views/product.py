from apps.shop.models import Product
from apps.api.views import ApiView


class ProductView(ApiView):
    model = Product

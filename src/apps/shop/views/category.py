from apps.shop.models import Category
from apps.api.views import ApiView


class CategoryView(ApiView):
    model = Category

from apps.shop.models import Manufacturer
from apps.api.views import ApiView


class ManufacturerView(ApiView):
    model = Manufacturer

from apps.sells.models import Sell
from django.conf import settings


class AllSellListUseCase:

    def execute(self):
        return self._factory()

    def _factory(self):
        self._sells = Sell.objects.all().order_by('-created_at')
        return self._sells


class SellsExistsUseCase:

    def __init__(self, filters: dict):
        self._filters = filters

    def execute(self):
        return self._factory()

    def _factory(self):
        self._exists = Sell.objects.filter(**self._filters).exists()
        return self._exists


class SellDetailsUseCase:

    def __init__(self, request, filters: dict):
        self._filters = filters
        self.request = request

    def execute(self):
        return self._factory()

    def execute_json_response(self):
        return self._factory_json_response()

    def _factory(self):
        self.sell = Sell.objects.filter(**self._filters).first()
        return self.sell

    def _factory_json_response(self):
        self.sell = Sell.objects.filter(**self._filters).first()
        if self.sell:
            sell_response = {
                'id': self.sell.id,
                'sell_date': self.sell.sell_date,
                'sell_price': self.sell.sell_price,
                'sell_image': self._get_absolute_url(self.sell.sell_image.url) if self.sell.sell_image else '',
                'sell_place': self.sell.sell_place,
                'buyer': self.sell.buyer,
                'sell_description': self.sell.sell_description,
                'created_at': self.sell.created_at,
                'updated_at': self.sell.updated_at,
            }
        else:
            sell_response = {}

        return sell_response

    def _get_absolute_url(self, relative_url):
        if self.request:
            return self.request.build_absolute_uri(relative_url)
        return f"{settings.SITE_URL}{relative_url}"


class SellUpdateUseCase:
    def __init__(self, sell_instance, update_data):
        self.sell_instance = sell_instance
        self._update_data = update_data

    def execute(self):
        return self._update_sell()

    def _update_sell(self):
        if self.sell_instance:
            for key, value in self._update_data.items():
                setattr(self.sell_instance, key, value)
            self.sell_instance.save()
            return self.sell_instance
        else:
            return None

# class SellUpdateUseCase:
#     def __init__(self, sell_instance, update_data):
#         self.sell_instance = sell_instance
#         self._update_data = update_data
#
#     def execute(self):
#         return self._update_sell()
#
#     def _update_sell(self):
#         if self.sell_instance:
#             for key, value in self._update_data.items():
#                 setattr(self.sell_instance, key, value)
#             self.sell_instance.save()
#             return self.sell_instance
#         else:
#             return None

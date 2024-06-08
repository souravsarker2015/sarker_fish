from apps.sells.models import Sell


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

    def __init__(self, filters: dict):
        self._filters = filters

    def execute(self):
        return self._factory()

    def _factory(self):
        self._user = Sell.objects.filter(**self._filters).first()
        return self._user

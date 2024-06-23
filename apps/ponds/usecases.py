from django.conf import settings

from apps.ponds.models import Pond


class AllPondListUseCase:

    def execute(self):
        return self._factory()

    def _factory(self):
        self._ponds = Pond.objects.all().order_by('-created_at')
        return self._ponds


class PondsExistsUseCase:

    def __init__(self, filters: dict):
        self._filters = filters

    def execute(self):
        return self._factory()

    def _factory(self):
        self._exists = Pond.objects.filter(**self._filters).exists()
        return self._exists


class PondDetailsUseCase:

    def __init__(self, request, filters: dict):
        self._filters = filters
        self.request = request

    def execute(self):
        return self._factory()

    def execute_json_response(self):
        return self._factory_json_response()

    def _factory(self):
        self.pond = Pond.objects.filter(**self._filters).first()
        return self.pond

    def _factory_json_response(self):
        self.pond = Pond.objects.filter(**self._filters).first()
        if self.pond:
            pond_response = {
                'id': self.pond.id,
                'name': self.pond.name,
                'location': self.pond.location,
            }
        else:
            pond_response = {}

        return pond_response

    def _get_absolute_url(self, relative_url):
        if self.request:
            return self.request.build_absolute_uri(relative_url)
        return f"{settings.SITE_URL}{relative_url}"


class PondUpdateUseCase:
    def __init__(self, pond_instance, update_data):
        self.pond_instance = pond_instance
        self._update_data = update_data

    def execute(self):
        return self._update_pond()

    def _update_pond(self):
        if self.pond_instance:
            for key, value in self._update_data.items():
                setattr(self.pond_instance, key, value)
            self.pond_instance.save()
            return self.pond_instance
        else:
            return None

# class PondUpdateUseCase:
#     def __init__(self, pond_instance, update_data):
#         self.pond_instance = pond_instance
#         self._update_data = update_data
#
#     def execute(self):
#         return self._update_pond()
#
#     def _update_pond(self):
#         if self.pond_instance:
#             for key, value in self._update_data.items():
#                 setattr(self.pond_instance, key, value)
#             self.pond_instance.save()
#             return self.pond_instance
#         else:
#             return None

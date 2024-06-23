from django.core.paginator import Paginator


class PondPagination:
    def __init__(self, ponds=None, page=None, per_page=None):
        self.ponds = ponds
        self.page = page
        self.per_page = per_page

    def execute(self):
        paginator = Paginator(self.ponds, self.per_page)  # Show 10 ponds per page.
        page_number = self.page
        page_obj = paginator.get_page(page_number)
        return page_obj


class GetPondUpdateRequestedData:
    def __init__(self, request):
        self.request = request

    def get_data(self):
        data = {
            'name': self.request.POST.get('name'),
            'location': self.request.POST.get('location'),
        }
        return data

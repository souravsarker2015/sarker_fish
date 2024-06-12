from django.core.paginator import Paginator


class Pagination:
    def __init__(self, sells=None, page=None, per_page=None):
        self.sells = sells
        self.page = page
        self.per_page = per_page

    def execute(self):
        paginator = Paginator(self.sells, self.per_page)  # Show 10 sells per page.
        page_number = self.page
        page_obj = paginator.get_page(page_number)
        return page_obj


class GetUpdateRequestedData:
    def __init__(self, request):
        self.request = request

    def get_data(self):
        data = {
            'sell_date': self.request.POST.get('sell_date'),
            'sell_price': self.request.POST.get('sell_price'),
            # 'sell_image': self.request.FILES.get('sell_image'),
            'sell_place': self.request.POST.get('sell_place'),
            'buyer': self.request.POST.get('buyer'),
            'sell_description': self.request.POST.get('sell_description'),
        }
        if self.request.FILES.get('sell_image') is not None:
            data['sell_image'] = self.request.FILES.get('sell_image')
        return data

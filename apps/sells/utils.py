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

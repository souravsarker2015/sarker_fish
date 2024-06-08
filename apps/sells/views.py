from django.shortcuts import render
from django.views import View

from apps.sells.models import Sell
from django.core.paginator import Paginator

from apps.sells.utils import Pagination


class SellListView(View):
    def get(self, request):
        sells = Sell.objects.all().order_by('-sell_date')
        # # Pagination logic
        # paginator = Paginator(sells, 10)  # Show 10 sells per page.
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        page_obj = Pagination(
            sells=sells,
            page=request.GET.get('page'),
            per_page=10
        ).execute()

        context = {'page_obj': page_obj}
        return render(request, 'sells/sell_list.html', context)

from django.shortcuts import render, redirect
from django.views import View

from apps.sells.forms import SellForm
from apps.sells.models import Sell
from django.core.paginator import Paginator

from apps.sells.utils import Pagination


class SellListView(View):
    def get(self, request):
        sells = Sell.objects.all().order_by('-created_at')
        for sell in sells:
            print(sell.created_at)
        page_obj = Pagination(sells=sells, page=request.GET.get('page'), per_page=10).execute()
        context = {'page_obj': page_obj}
        return render(request, 'sells/sell_list.html', context)

    def post(self, request, *args, **kwargs):
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sells')
        return render(request, 'sells/sell_list.html', {'form': form, 'form_error_exists': True})

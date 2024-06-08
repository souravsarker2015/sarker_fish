from django.shortcuts import render, redirect
from django.views import View
from apps.sells.forms import SellForm
from apps.sells.usecases import AllSellListUseCase
from apps.sells.utils import Pagination


class SellListView(View):
    def get(self, request):
        sells = AllSellListUseCase().execute()
        page_obj = Pagination(sells=sells, page=request.GET.get('page'), per_page=10).execute()
        context = {'page_obj': page_obj}
        return render(request, 'sells/sell_list.html', context)

    def post(self, request, *args, **kwargs):
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sells')
        else:
            sells = AllSellListUseCase().execute()
            page_obj = Pagination(sells=sells, page=request.GET.get('page'), per_page=10).execute()
            context = {
                'page_obj': page_obj,
                'form': form,
                'form_error_exists': True,
            }
            return render(request, 'sells/sell_list.html', context)

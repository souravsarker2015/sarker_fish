from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from apps.sells.forms import SellForm
from apps.sells.usecases import AllSellListUseCase, SellDetailsUseCase, SellUpdateUseCase
from apps.sells.utils import Pagination, GetUpdateRequestedData


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
                'form_creation_error_exists': True,
            }
            return render(request, 'sells/sell_list.html', context)


class SellDetails(View):
    def get(self, request, *args, **kwargs):
        sell_id = kwargs.get('id')
        sell_json_response = SellDetailsUseCase(request, {'id': sell_id}).execute_json_response()
        return JsonResponse({'success': True, 'data': sell_json_response})

    def post(self, request, *args, **kwargs):
        form = SellForm(request.POST, request.FILES)
        sell_id = kwargs.get('id')
        if form.is_valid():
            sell = SellDetailsUseCase(request, {'id': sell_id}).execute()
            update_data = GetUpdateRequestedData(request).get_data()
            SellUpdateUseCase(sell, update_data).execute()
            return redirect('sells')
        else:
            sells = AllSellListUseCase().execute()
            sell = SellDetailsUseCase(request, {'id': sell_id}).execute()
            page_obj = Pagination(sells=sells, page=request.GET.get('page'), per_page=10).execute()
            context = {'page_obj': page_obj, 'form': form, 'form_update_error_exists': True, 'sell': sell}
            return render(request, 'sells/sell_list.html', context)

    def delete(self, request, *args, **kwargs):
        sell_id = kwargs.get('id')
        sell = SellDetailsUseCase(request, {'id': sell_id}).execute()
        if sell:
            sell.delete()
            # return redirect('sells')
            return JsonResponse({'success': True, 'data': {'id': sell_id}})
        else:
            return JsonResponse({'success': False, 'data': {'id': sell_id}})
            # messages.add_message(
            #     request,
            #     messages.ERROR,
            #     'Sell not found',
            #     extra_tags='sell_not_found'
            # )
            # return redirect('sells')

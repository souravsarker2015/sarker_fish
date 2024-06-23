from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from apps.ponds.forms import PondForm
from apps.ponds.usecases import AllPondListUseCase, PondDetailsUseCase, PondUpdateUseCase
from apps.ponds.utils import PondPagination, GetPondUpdateRequestedData


class PondListView(View):
    def get(self, request):
        ponds = AllPondListUseCase().execute()
        page_obj = PondPagination(ponds=ponds, page=request.GET.get('page'), per_page=10).execute()
        context = {'page_obj': page_obj}
        return render(request, 'ponds/pond_list.html', context)

    def post(self, request, *args, **kwargs):
        form = PondForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ponds')
        else:
            ponds = AllPondListUseCase().execute()
            page_obj = PondPagination(ponds=ponds, page=request.GET.get('page'), per_page=10).execute()
            context = {
                'page_obj': page_obj,
                'form': form,
                'form_creation_error_exists': True,
            }
            return render(request, 'ponds/pond_list.html', context)


class PondDetails(View):
    def get(self, request, *args, **kwargs):
        pond_id = kwargs.get('id')
        pond_json_response = PondDetailsUseCase(request, {'id': pond_id}).execute_json_response()
        return JsonResponse({'success': True, 'data': pond_json_response})

    def post(self, request, *args, **kwargs):
        form = PondForm(request.POST)
        pond_id = kwargs.get('id')
        if form.is_valid():
            pond = PondDetailsUseCase(request, {'id': pond_id}).execute()
            update_data = GetPondUpdateRequestedData(request).get_data()
            PondUpdateUseCase(pond, update_data).execute()
            return redirect('ponds')
        else:
            ponds = AllPondListUseCase().execute()
            pond = PondDetailsUseCase(request, {'id': pond_id}).execute()
            page_obj = PondPagination(ponds=ponds, page=request.GET.get('page'), per_page=10).execute()
            context = {'page_obj': page_obj, 'form': form, 'form_update_error_exists': True, 'pond': pond}
            return render(request, 'ponds/pond_list.html', context)

    def delete(self, request, *args, **kwargs):
        pond_id = kwargs.get('id')
        pond = PondDetailsUseCase(request, {'id': pond_id}).execute()
        if pond:
            pond.delete()
            return JsonResponse({'success': True, 'data': {'id': pond_id}})
        else:
            return JsonResponse({'success': False, 'data': {'id': pond_id}})

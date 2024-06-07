from django.shortcuts import render
from django.views import View


class SellListView(View):
    def get(self, request):
        return render(request, 'sells/sell_list.html')

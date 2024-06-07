from django.shortcuts import render
from django.views import View


class CreditorListView(View):
    def get(self, request):
        return render(request, 'creditors/creditor_list.html')

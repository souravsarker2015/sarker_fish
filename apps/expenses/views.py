from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class ExpenseListView(View):
    def get(self, request):
        return render(request, 'expenses/expense_list.html')

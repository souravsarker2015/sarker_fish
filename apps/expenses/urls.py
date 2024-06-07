from django.urls import path

from apps.expenses.views import ExpenseListView

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
]

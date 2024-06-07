from django.urls import path

from apps.creditors.views import CreditorListView

urlpatterns = [
    path('', CreditorListView.as_view(), name='creditor_list'),
]

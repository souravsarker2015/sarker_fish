from django.urls import path

from apps.sells.views import SellListView

urlpatterns = [
    path('', SellListView.as_view(), name='sell_list'),
]

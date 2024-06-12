from django.urls import path

from apps.sells import views

urlpatterns = [
    path('', views.SellListView.as_view(), name='sells'),
    path('<int:id>/', views.SellDetails.as_view(), name='sells'),
]

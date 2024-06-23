from django.urls import path

from apps.ponds import views

urlpatterns = [
    path('', views.PondListView.as_view(), name='ponds'),
    path('<int:id>/', views.PondDetails.as_view(), name='ponds'),
]

from django.urls import path

from api.customer.views import CustomerCreateAPIView, CustomerListAPIView

urlpatterns = [
    path('create', CustomerCreateAPIView.as_view(), name='create'),
    path('list', CustomerListAPIView.as_view(), name='list')
]

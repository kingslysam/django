from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view

from CMS.models import Customer
from api.customer.serializers import CustomerSerializer


class CustomerCreateAPIView(CreateAPIView):
    serializer_class = CustomerSerializer


class CustomerListAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateAPI(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDeleteAPI(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerFull(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

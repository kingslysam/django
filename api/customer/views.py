from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.decorators import api_view

from CMS.models import Customer
from api.customer.serializers import CustomerSerializer


class CustomerCreateAPIView(CreateAPIView):
    serializer_class = CustomerSerializer


class CustomerListAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

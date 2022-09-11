from django.shortcuts import render
from collections import Counter
from django.http import HttpResponse
from itertools import chain
from .form import CustomerCreateForm
from .models import Customer, Transaction
from django.views.generic import CreateView, DetailView, ListView, TemplateView, FormView


# Create your views here.
class CMISHomeView(TemplateView):
    template_name = 'base.html'


def customer(request):
    cus = Customer.objects.all().order_by('account_number')
    return render(request, 'cms/customer.html', {'cus': cus})


def transaction(request):
    transact = Transaction.objects.all().latest('transaction_amount').transaction_amount
    return render(request, 'cms/transaction.html', {'transact': transact})


class EditTemplate(TemplateView):
    template_name = 'cms/edit.html'


class CustomerAdd(CreateView):
    model = Customer
    template_name = 'cms/add_customer.html'
    fields = ['account_number', 'account_name', 'account_holder_name',
              'customer_birth_date', 'customer_nida', 'customer_role']
    context_object_name = 'customers'
    success_url = '/customer'


class CustomerDetails(DetailView):
    model = Customer
    template_name = 'cms/profile.html'


class CustomerFormDjango(FormView):
    template_name = 'cms/djangoform.html'
    form_class = CustomerCreateForm
    success_url = '/customer'


class CustomerMobile(DetailView):
    model = Customer
    template_name = 'mobile/myHome.html'


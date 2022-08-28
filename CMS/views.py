from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Loan, Transaction
from django.views.generic import CreateView, DetailView, ListView


# Create your views here.

def customer(request):
    cus = Customer.objects.all().order_by('account_number')
    return render(request, 'cms/customer.html', {'cus': cus})


class CustomerListView(ListView):
    queryset = Transaction.objects.all()
    model = Transaction
    template_name = 'cms/profile.html'
    context_object_name = 'transactions'
    success_url = '/profile'

    def get_queryset(self):
        query = Transaction.objects.filter(account_number='COOPERATE')
        return query


def loan(request):
    loans = Loan.objects.all().order_by('loan_amount')
    return render(request, 'cms/loan.html', {'loans': loans})


def transaction(request):
    transact = Transaction.objects.all()
    return render(request, 'cms/transaction.html', {'transact': transact})


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

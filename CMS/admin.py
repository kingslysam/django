from django.contrib import admin
from .models import Customer, Transaction, Account, CustomerAccount, Service, CustomerService
# Register your models here.

admin.site.register([
    Customer,
    Transaction,
    Account,
    CustomerAccount,
    Service,
    CustomerService
])

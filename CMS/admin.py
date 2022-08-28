from django.contrib import admin
from .models import Customer,Transaction,Account,Loan,NextOfKin,Staff,StaffCustomer,CustomerAccount
# Register your models here.

admin.site.register([
    Customer,
    Transaction,
    Account,
    Loan,
    NextOfKin,
    Staff,
    StaffCustomer,
    CustomerAccount
])

from django.db import models


# Create your models here.
class Customer(models.Model):
    account_number = models.IntegerField(unique=True, primary_key=True)
    account_name = models.CharField(max_length=255)
    account_holder_name = models.CharField(max_length=255)
    customer_birth_date = models.DateField()
    customer_nida = models.IntegerField(unique=True, verbose_name="NO NIDA")
    customer_role = models.CharField(max_length=20, verbose_name="Normal")
    customer_occupation = models.CharField(max_length=100, default="Not Enter")

    def __str__(self):
        return self.account_name

    def __int__(self):
        return self.account_number


class Transaction(models.Model):
    transaction_number = models.IntegerField(unique=True, primary_key=True)
    account_number = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_amount = models.FloatField()
    transaction_type = models.CharField(max_length=50)


class Account(models.Model):
    account_id = models.IntegerField(unique=True, primary_key=True)
    account_name = models.CharField(unique=True, max_length=50)
    account_desc = models.CharField(unique=True, max_length=200)
    account_currency = models.CharField(max_length=15)
    number_of_accounts = models.IntegerField


class Loan(models.Model):
    account_number = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    loan_type = models.CharField(max_length=20)
    loan_start_date= models.DateField()
    loan_duration = models.IntegerField()
    loan_interest_rate = models.IntegerField()
    loan_amount_paid = models.FloatField()

    def __int__(self):
        return self.account_number


class NextOfKin(models.Model):
    account_number = models.ForeignKey(Customer, on_delete=models.CASCADE)
    next_of_kin_name = models.CharField(max_length=255, unique=True)
    next_of_kin_contact = models.CharField(max_length=15)
    next_of_kin_residence = models.CharField(max_length=25)
    next_of_kin_nida = models.IntegerField(unique=True)


class Staff(models.Model):
    staff_id = models.IntegerField(unique=True)
    staff_name = models.CharField(max_length=255)
    staff_position = models.CharField(max_length=255)


class StaffCustomer(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    account_number = models.ForeignKey(Customer, on_delete=models.CASCADE)


class CustomerAccount(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    account_number = models.ForeignKey(Customer, on_delete=models.CASCADE)
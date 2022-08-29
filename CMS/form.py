from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy
from django.forms import Form
from django import forms
from crispy_forms.layout import Submit


CUSTOMER_ROLE = [('Not enter','Select'),('Normal', 'Normal'), ('High', 'High')]


class CustomerCreateForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('customer')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-success'))

    account_number = forms.IntegerField(widget=forms.NumberInput)
    account_name = forms.CharField(max_length=200, widget=forms.TextInput)
    customer_name = forms.CharField(max_length=100, required=True, label='Customer name')
    customer_birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    customer_nida = forms.IntegerField(widget=forms.NumberInput)
    customer_role = forms.ChoiceField(choices=CUSTOMER_ROLE, widget=forms.Select)
    customer_occupation = forms.CharField(widget=forms.TextInput)




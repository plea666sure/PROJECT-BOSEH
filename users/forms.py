from django import forms
from .models import Customer, Akun

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['nama_customer', 'telepon_customer', 'alamat_customer']

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

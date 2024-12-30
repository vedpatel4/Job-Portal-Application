from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Address'}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website'}))
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_number', 'email', 'website']

from django import forms
from .models import Job

class Create_JobForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))
    salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}))
    job_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Type'}))


    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary', 'job_type']

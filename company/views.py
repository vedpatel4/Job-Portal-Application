from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm
from django.contrib.auth.decorators import login_required

@login_required
def register(request):
    form = CompanyForm()

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('/')

    context = {'registerform': form}
    return render(request, 'company/register.html', context=context)

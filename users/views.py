from django.shortcuts import render, redirect
from . forms import CreateUserForm,LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from company.models import Company


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    context = {'signupform': form}

    return render(request, 'users/signup.html', context=context)



def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                if not Company.objects.filter(user=user).exists():
                    return redirect("company_register") # Redirect to company registration if not registered
                return redirect("show")  # Redirect to show page if company is registered
    
    context = {'loginform': form}
    return render(request, 'users/login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect("login") # Redirect to login page after logout
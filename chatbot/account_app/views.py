from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


def home_view(request):
    home = True
    return render(request, 'home.html', {'home': home})


def register_view(request):
    reg = True
    if request.method == 'POST':
        register_form = RegisterUser(request.POST)
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            obj = UserAccount(name=name, username=username, email=email, password=make_password(password))
            obj.save()
            return redirect('account:login')
    else:
        register_form = RegisterUser()
    return render(request, 'account_app/register.html', {'form': register_form, 'register': reg, 'errors': register_form.errors})


def login_view(request):
    log = True
    if request.method == 'POST':
        login_form = LoginUser(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            obj = UserAccount.objects.filter(username=username).first()
            if obj is None:
                return render(request, 'account_app/login.html', {'error': "Username does not exist"})
            else:
                if check_password(password, obj.password):
                    token = SessionToken(username=obj)
                    token.create_token()
                    token.save()
                    response = redirect('chat:script')
                    response.set_cookie(key='SessionToken', value=token.token)
                    return response
                else:
                    messages.error(request, "Wrong Password")
        else:
            messages.error(request, "Invalid input")
            return render(request, 'account_app/login.html')
    else:
        login_form = LoginUser()
    return render(request, 'account_app/login.html', {'form': login_form, 'login': log})


def check_validation(request):
    if request.COOKIES.get('SessionToken'):
        session = SessionToken.objects.filter(token=request.COOKIES.get('SessionToken')).first()
        if session:
            return session.username
    else:
        return None


def logout_view(request):
    user = check_validation(request)
    if user:
        token = SessionToken.objects.filter(username=user)
        token.delete()
        return redirect('account:home')
    else:
        return redirect('account:login')




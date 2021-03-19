from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def cadastro(request):
    messages.info(request, 'Nada Postado')
    if request.method != "POST":
        return render(request, 'accounts/cadastro.html')
    return render(request, 'accounts/cadastro.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

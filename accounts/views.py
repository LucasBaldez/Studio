from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import Usuarios


def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def cadastro(request):
    if request.method != "POST":
        return render(request, 'accounts/cadastro.html')


    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido!')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'A Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'O Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request,'Registrado com sucesso! Favor logar.')
    user = Usuarios(nome=nome,sobrenome=sobrenome, usuario=usuario, email = email,senha=senha)
    user.save()
    return redirect('login')

def dashboard(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'accounts/dashboard.html', {'usuarios' : usuarios })

def ver_usuario(request, usuario_id):
    ##contato = Contato.objects.get(id=contato_id)
    usuario = get_object_or_404(Usuarios,id=usuario_id) #tratamento de erro se o ID não for encontrado
    return render(request, 'accounts/ver_usuario.html', {
        'usuario' : usuario
    })

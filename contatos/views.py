from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato, Procedimento
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos' : contatos
    })

def ver_contato(request, contato_id):
    ##contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato,id=contato_id) #tratamento de erro se o ID não for encontrado]
    procedimentos = contato.procedimento.all() #pega todos os procedimentos do contato
    return render(request, 'contatos/ver_contato.html', {
        'contato' : contato,
        'procedimentos' : procedimentos
    })

def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio!'
        )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo)
    )

    return render(request, 'contatos/busca.html',{
        'contatos' : contatos
    })
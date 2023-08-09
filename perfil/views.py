from django.shortcuts import render, HttpResponse, redirect
from .models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from .utils import calcular_total

# Create your views here.
def home(request):
    contas = Conta.objects.all()
    total = calcular_total(contas, 'valor')
    return render(request, 'home.html', {'contas': contas, 'total': total})

def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    total = calcular_total(contas, 'valor')
    return render(request, 'gerenciar.html', {'contas': contas, 'total': total, 'categorias': categorias})

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')

    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.WARNING, 'Preencha todos os campos!')
        return redirect('/perfil/gerenciar/')

    conta = Conta(
        apelido = apelido,
        banco = banco,
        valor = valor,
        icone = icone
    )

    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Dados salvo com sucesso!')
    return redirect('/perfil/gerenciar/')

def deletar_banco(request, id):
    conta = Conta.objects.get(id=id)
    conta.delete()
    messages.add_message(request, constants.SUCCESS, 'Conta deletada com sucesso!')
    return redirect('/perfil/gerenciar/')
    
def cadastrar_categoria(request):
    categoria = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    if len(categoria.strip()) == 0:
        messages.add_message(request, constants.WARNING, 'Preencha o nome da categoria!')
        return ('/perfil/gerenciar/')
    
    categoria = Categoria(
        categoria = categoria,
        essencial = essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria salva com sucesso!')
    return redirect('/perfil/gerenciar/')

def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.essencial = not categoria.essencial

    categoria.save()

    return redirect('/perfil/gerenciar/')
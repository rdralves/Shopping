from django.shortcuts import render
from Site.form import ClienteForm

from Site.models import Departamento, Produto

# Create your views here.
def index(request):
    departamento = Departamento.objects.all()
    produtotos_em_destaque = Produto.objects.filter(destaque = True)
    context = {
        'departamentos': departamento,
        'produtos': produtotos_em_destaque,
    }
    return render(request, "index.html", context)


def produto_lista(request):
    departamento = Departamento.objects.all()
    produtos = Produto.objects.all()
    context = {
        'departamentos': departamento,
        'produtos': produtos,
        'nome_categoria': 'Todos Produtos',
    }
    return render(request, 'produtos.html', context)

def produto_lista_por_id(request, id):
    departamento = Departamento.objects.all()
    produtos_por_departamento = Produto.objects.filter(departamento_id =id)
    categoria = departamento.get(id = id).nome
    context = {
        'departamentos': departamento,
        'produtos': produtos_por_departamento,
        'nome_categoria':categoria
    }
    return render(request, 'produtos.html', context)


def produto_detalhe(request, id):
    departamentos = Departamento.objects.all()
    produto = Produto.objects.get(id=id)
    produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento.id)
    context = {
        'departamentos': departamentos,
        'produto': produto,
        'produtos_relacionados': produtos_relacionados,
    }
    return render(request, 'produto_detalhes.html', context)


def institucional(request):
    departamento = Departamento.objects.all()
    context = {
        'departamentos': departamento,
    }
    return render(request, 'empresa.html', context)


def cadastro(request):
    departamentos = Departamento.objects.all()
    
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = formulario.save()
            formulario = ClienteForm()
    else:
        formulario = ClienteForm()

    context = {
        'departamentos': departamentos,
        'form_cliente' : formulario
    }
    return render(request, 'cadastro.html', context)


def contato(request):
    departamento = Departamento.objects.all()
    context = {
        'departamentos': departamento,
    }
    return render(request, 'contato.html', context)
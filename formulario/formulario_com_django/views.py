from django.shortcuts import get_object_or_404, redirect, render
from django.forms import ModelForm
from .models import *


# Create your views here.


class Formulario_Cadastro(ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'email', 'sexo', 'endereco', 'cpf']


def lista_pessoas(request, template_name='lista_pessoas.html'):
    Cadastro = Formulario.objects.all()
    cadastrados = {'lista': Cadastro}
    return render(request, template_name, cadastrados)


def cadastro(request, template_name='cadastro_pessoas.html'):
    form = Formulario_Cadastro(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request, template_name, {'form': form})


def editar_cadastro(request, pk, template_name='cadastro_pessoas.html'):
    pessoa = get_object_or_404(Formulario, pk=pk)
    print('chegou aqui', pessoa.email)
    if request.method == "POST":
        form = Formulario_Cadastro(request.POST, instance=pessoa)
        print('cheguei aqui no if ')
        if form.is_valid():
            pessoa = form.save()
            return redirect('lista_pessoas')
    else:
        print('cheguei aqui no else')
        form = Formulario_Cadastro(request.POST or None, instance=pessoa)
    return render(request, template_name, {'form': form})


def remover_pessoa(request,pk):
    pessoa = Formulario.objects.get(pk=pk)
    if request.method == "POST":
        pessoa.delete()
        redirect('lista_pessoas')
    render(request, 'livro_delete.html', {'pessoa': pessoa})

    render(request, 'livro_delete.html', {'pessoa': pessoa})
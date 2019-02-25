from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (
	Pessoa, 
	Veiculo, 
	MovRotativo,
	Mensalista,
	MovMensalista,
	)
from .forms import (
	PessoaForm,
	VeiculoForm,
	MovRotativoForm,
	)


def home(request):
	context = {'mensagem':'Ola mundo111111111'}
	return render(request, 'core/index.html', context)


def lista_pessoas(request):
	pessoas = Pessoa.objects.all() 
	form = PessoaForm()
	data = {'pessoas': pessoas, 'form': form}
	return render(request, 'core/lista_pessoas.html', data)


def cadastra_pessoas(request):
	form = PessoaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_pessoas')


def lista_veiculos(request):
	veiculos = Veiculo.objects.all() 
	form = VeiculoForm()
	data = {'veiculos': veiculos, 'form': form}
	return render(request, 'core/lista_veiculos.html', data)


def cadastra_veiculos(request):
	form = VeiculoForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_veiculos')


def lista_mov_rotativos(request):
	mov_rotativos = MovRotativo.objects.all() 
	form = MovRotativoForm()
	data = {'mov_rotativos': mov_rotativos, 'form':form}
	return render(request, 'core/lista_mov_rotativos.html', data)


def cadastra_mov_rotativos(request):
	form = MovRotativoForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_mov_rotativos')


def lista_mensalistas(request):
	mensalistas = Mensalista.objects.all() 
	return render(request, 'core/lista_mensalistas.html', 
		{'mensalistas': mensalistas})


def lista_mov_mensalistas(request):
	mov_mensalistas = MovMensalista.objects.all() 
	return render(request, 'core/lista_mov_mensalistas.html', 
		{'mov_mensalistas': mov_mensalistas})

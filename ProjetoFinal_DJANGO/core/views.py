from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
	MensalistaForm,
	MovMensalistaForm,
	)


@login_required
def home(request):
	return render(request, 'core/index.html')


@login_required
def lista_pessoas(request):
	pessoas = Pessoa.objects.all() 
	form = PessoaForm()
	data = {'pessoas': pessoas, 'form': form}
	return render(request, 'core/lista_pessoas.html', data)


@login_required
def cadastra_pessoas(request):
	form = PessoaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_pessoas')


@login_required
def update_pessoas(request, id):
	data = {}
	pessoa = Pessoa.objects.get(id=id)
	form = PessoaForm(request.POST or None, instance=pessoa)
	data['pessoa'] = pessoa
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_pessoas')
	else:
		return render(request, 'core/update_pessoas.html', data)


@login_required
def delete_pessoas(request, id):
	data = {}
	pessoa = Pessoa.objects.get(id=id)
	if request.method == 'POST':
		pessoa.delete()
		return redirect('core_lista_pessoas')
	else:
		return render(request, 'core/delete_confirm.html', {'obj': pessoa})


@login_required
def lista_veiculos(request):
	veiculos = Veiculo.objects.all() 
	form = VeiculoForm()
	data = {'veiculos': veiculos, 'form': form}
	return render(request, 'core/lista_veiculos.html', data)


@login_required
def cadastra_veiculos(request):
	form = VeiculoForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_veiculos')


@login_required
def update_veiculos(request, id):
	data = {}
	veiculo = Veiculo.objects.get(id=id)
	form = VeiculoForm(request.POST or None, instance=veiculo)
	data['veiculo'] = veiculo
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_veiculos')
	else:
		return render(request, 'core/update_veiculos.html', data)


@login_required
def delete_veiculos(request, id):
	data = {}
	veiculo = Veiculo.objects.get(id=id)
	if request.method == 'POST':
		veiculo.delete()
		return redirect('core_lista_veiculos')
	else:
		return render(request, 'core/delete_confirm.html', 
			{'obj': veiculo})


@login_required
def lista_mov_rotativos(request):
	mov_rotativos = MovRotativo.objects.all() 
	form = MovRotativoForm()
	data = {'mov_rotativos': mov_rotativos, 'form': form}
	return render(request, 'core/lista_mov_rotativos.html', data)


@login_required
def cadastra_mov_rotativos(request):
	form = MovRotativoForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_mov_rotativos')


@login_required
def update_rotativos(request, id):
	data = {}
	rotativo = MovRotativo.objects.get(id=id)
	form = MovRotativoForm(request.POST or None, instance=rotativo)
	data['rotativo'] = rotativo
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_mov_rotativos')
	else:
		return render(request, 'core/update_rotativos.html', data)


@login_required
def delete_rotativos(request, id):
	data = {}
	rotativo = MovRotativo.objects.get(id=id)
	if request.method == 'POST':
		rotativo.delete()
		return redirect('core_lista_mov_rotativos')
	else:
		return render(request, 'core/delete_confirm.html', 
			{'obj': rotativo})


@login_required
def lista_mensalistas(request):
	mensalistas = Mensalista.objects.all() 
	form = MensalistaForm()
	data = {'mensalistas': mensalistas, 'form': form}
	return render(request, 'core/lista_mensalistas.html', data)


@login_required
def cadastra_mensalistas(request):
	form = MensalistaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_mensalistas')


@login_required
def update_mensalistas(request, id):
	data = {}
	mensalista = Mensalista.objects.get(id=id)
	form = MensalistaForm(request.POST or None, instance=mensalista)
	data['mensalista'] = mensalista
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_mensalistas')
	else:
		return render(request, 'core/update_mensalistas.html', data)


@login_required
def delete_mensalistas(request, id):
	data = {}
	mensalista = Mensalista.objects.get(id=id)
	if request.method == 'POST':
		mensalista.delete()
		return redirect('core_lista_mensalistas')
	else:
		return render(request, 'core/delete_confirm.html', 
			{'obj': mensalista})


@login_required
def lista_mov_mensalistas(request):
	mov_mensalistas = MovMensalista.objects.all() 
	form = MovMensalistaForm()
	data = {'mov_mensalistas': mov_mensalistas, 'form': form}
	return render(request, 'core/lista_mov_mensalistas.html', data)


@login_required
def cadastra_mov_mensalistas(request):
	form = MovMensalistaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_mov_mensalistas')


@login_required
def update_mov_mensalistas(request, id):
	data = {}
	mov_mensalista = MovMensalista.objects.get(id=id)
	form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
	data['mov_mensalista'] = mov_mensalista
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_mov_mensalistas')
	else:
		return render(request, 'core/update_mov_mensalistas.html', data)


@login_required
def delete_mov_mensalistas(request, id):
	data = {}
	mov_mensalista = MovMensalista.objects.get(id=id)
	if request.method == 'POST':
		mov_mensalista.delete()
		return redirect('core_lista_mov_mensalistas')
	else:
		return render(request, 'core/delete_confirm.html', 
			{'obj': mov_mensalista})

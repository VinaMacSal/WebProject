from django.shortcuts import render
from .models import Contato

def home(request):
	return render(request, 'website/index.html')


def planos(request):
	return render(request, 'website/planos.html')


def servicos(request):
	return render(request, 'website/servicos.html')


def contato(request):
	mensagem = ''
	if request.method == 'POST':
		try:
			contato = {}
			contato['nome'] = request.POST.get('nome')
			contato['email'] = request.POST.get('email')
			contato['telefone'] = request.POST.get('telefone')
			contato['mensagem'] = request.POST.get('mensagem')
			Contato.objects.create(**contato)
		except Exception as e:
			mensagem = str(e)
		else:
			mensagem = "Contato Realizado com Sucesso"
	return render(request, 'website/contato.html', {'mensagem': mensagem})


def sobre(request):
	return render(request, 'website/sobre.html')

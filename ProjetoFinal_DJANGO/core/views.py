from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	context = {'mensagem':'Ola mundo111111111'}
	return render(request, 'base.html', context)

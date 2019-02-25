from django.urls import path
from .views import (
	home, 
	lista_pessoas, 
	lista_veiculos, 
	lista_mov_rotativos,
	lista_mensalistas,
	lista_mov_mensalistas,
	cadastra_pessoas,
	cadastra_veiculos,
	cadastra_mov_rotativos,
	)

urlpatterns = [
    path('', home, name="core_home"),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('cadastra_pessoas/', cadastra_pessoas, name='core_cadastra_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('cadastra_veiculos/', cadastra_veiculos, name='core_cadastra_veiculos'),
    path('rotativos/', lista_mov_rotativos, name='core_lista_mov_rotativos'),
    path('cadastra_rotativos/', cadastra_mov_rotativos, name='core_cadastra_mov_rotativos'),
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensal/', lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    ]
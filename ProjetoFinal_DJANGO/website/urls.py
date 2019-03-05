from django.urls import path
from .views import (
	home,
	planos,
	servicos,
	contato,
	sobre,
	)
	
urlpatterns = [
    path('', home, name="website_home"),
    path('planos/', planos, name="website_planos"),
    path('servicos/', servicos, name="website_servicos"),
    path('contato/', contato, name="website_contato"),
    path('sobre/', sobre, name="website_sobre"),
    ]
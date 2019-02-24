from django.contrib import admin
from .models import (Marca, 
	Veiculo, 
	Pessoa, 
	Parametros, 
	MovRotativo,
	Mensalista,
	MovMensalista,
	)


class MovRotativoAdmin(admin.ModelAdmin):
	#def mostrar_veiculo(self, obj):
		#return obj.veiculo.placa + " - " + str(obj.veiculo.marca)
	
	#mostrar_veiculo.admin_order_field = 'veiculo'
	#mostrar_veiculo.short_description = 'Veiculo'

	list_display = ('veiculo', 'checkin', 'checkout', 
		"valor_hora", 'pago', 'total',
		'horas_total')


class MovMensalistaAdmin(admin.ModelAdmin):
	list_display = ('mensalista', 'dt_pgto', 'total')


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)
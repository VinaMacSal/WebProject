from django.contrib import admin
from .models import (Marca, 
	Veiculo, 
	Pessoa, 
	Parametros, 
	MovRotativo,
	)


class MovRotativoAdmin(admin.ModelAdmin):
	def mostrar_veiculo(self, obj):
		return obj.veiculo.placa + " - " + str(obj.veiculo.marca)
	mostrar_veiculo.admin_order_field = 'veiculo'
	mostrar_veiculo.short_description = 'Veiculo'

	list_display = ('mostrar_veiculo', 'checkin', 'checkout', 
		"valor_hora", 'pago', 'total',
		'horas_total')


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
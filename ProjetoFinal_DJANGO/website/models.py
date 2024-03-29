from django.db import models


class Contato(models.Model):
	nome = models.CharField(max_length=100)
	email = models.EmailField()
	telefone = models.CharField(max_length=100)
	mensagem = models.TextField()

	def __str__(self):
		return self.nome
from django.db import models


class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    periodicidade_meses = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

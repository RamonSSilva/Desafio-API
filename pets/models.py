from django.db import models
from accounts.models import Responsavel


class Pet(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    responsavel = models.ForeignKey(
        Responsavel,
        on_delete=models.CASCADE,
        related_name='pets'
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

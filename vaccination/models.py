from django.db import models
from pets.models import Pet
from vaccines.models import Vacina


class Vacinacao(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='vacinacoes'
    )
    vacina = models.ForeignKey(
        Vacina,
        on_delete=models.CASCADE
    )
    data_aplicacao = models.DateField()
    proxima_dose = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet.nome} - {self.vacina.nome}"

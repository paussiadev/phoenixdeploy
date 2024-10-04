from django.db import models
from material.models import Material
from roupa.models import Roupa

# Create your models here.
class Movimentacao(models.Model):
    codigo_material = models.ForeignKey(Material, on_delete = models.CASCADE, verbose_name="Nome", null= False, blank= False)
    codigo_roupa = models.ForeignKey(Roupa, on_delete = models.CASCADE, verbose_name="Código da Roupa", null= False, blank= False)
    quantidade = models.DecimalField(verbose_name="Quantidade", null=True, blank=True, max_digits=10, decimal_places=2)
    data = models.DateTimeField()
    valor_total = models.DecimalField(verbose_name="Valor Total",max_digits=10, decimal_places=2)
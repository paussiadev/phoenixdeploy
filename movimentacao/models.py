from django.db import models
from material.models import Material


# Create your models here.
class Movimentacao(models.Model):
    codigo_material = models.ForeignKey(Material, on_delete = models.CASCADE, verbose_name="Nome", null= False, blank= False)
    quantidade = models.DecimalField(verbose_name="Quantidade", null=True, blank=True, max_digits=10, decimal_places=2)
    data = models.DateField()
    valor_total = models.DecimalField(verbose_name="Valor Total",max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.quantidade and self.valor_total:
            material = self.codigo_material
            material.valor = self.valor_total / self.quantidade
            material.save()
        
        super().save(*args, **kwargs)
from django.db import models
from django.apps import apps 
from django.db.models import F, Sum

class Roupa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    imagem = models.ImageField(upload_to="fotos/")
    
    def __str__(self) -> str:
        return self.nome
    
    def valor_producao(self):
        # Importa o modelo RoupaMaterial para acessar os materiais e suas quantidades
        RoupaMaterial = apps.get_model('roupa', 'RoupaMaterial')
        
        # Calcula o valor total multiplicando o valor do material pela quantidade usada
        valor_total = RoupaMaterial.objects.filter(roupa=self).aggregate(
            total_valor=Sum(F('material__valor') * F('quantidade'))
        )['total_valor'] or 0

        return valor_total


class RoupaMaterial(models.Model):
    roupa = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    material = models.ForeignKey('material.Material', on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.roupa.nome


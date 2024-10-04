from django.db import models
from material.models import Material

# Create your models here.
class Roupa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    imagem = models.ImageField(upload_to="fotos/")
    materiais = models.ManyToManyField(Material, through='RoupaMaterial')


class RoupaMaterial(models.Model):
    roupa = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.roupa
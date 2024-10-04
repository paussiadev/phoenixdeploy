from django.db import models

# Create your models here.
class Material(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    unid_medida = models.CharField(verbose_name="Unidade de Medida", max_length=30, null=False, blank=True)
    valor = models.DecimalField(verbose_name="Valor", null=False, blank=False, max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to="fotos/")
    
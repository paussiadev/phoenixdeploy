from django.db import models
from django.db.models import Sum, F
from django.apps import apps

from roupa.models import RoupaMaterial  # Importação para carregar modelos dinamicamente

class Material(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100, null=False, blank=False)
    descricao = models.TextField(verbose_name="Descrição", null=True, blank=True)
    unid_medida = models.CharField(verbose_name="Unidade de Medida", max_length=30, null=False, blank=True)
    valor = models.DecimalField(verbose_name="Valor", null=False, blank=False, max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to="fotos/")

    def __str__(self) -> str:
        return self.nome

    def estoque_atual(self):
    # Importar os modelos necessários
        Movimentacao = apps.get_model('movimentacao', 'Movimentacao')
        RoupaMaterial = apps.get_model('roupa', 'RoupaMaterial')
        Producao = apps.get_model('producao', 'Producao')

    # Soma de todas as movimentações (entradas de estoque)
        movimentacao_estoque = Movimentacao.objects.filter(codigo_material=self).aggregate(Sum  ('quantidade'))
        estoque_movimentacao = movimentacao_estoque['quantidade__sum'] or 0

    # Soma de todas as produções que utilizaram o material
    # Multiplicando a quantidade da produção pela quantidade de material usado em cada roupa
        producao_estoque = RoupaMaterial.objects.filter(
        material=self,
        roupa__in=Producao.objects.values_list('roupa', flat=True)  # Apenas roupas que foram produzidas
        ).annotate(
        material_usado=F('quantidade') * F('roupa__producao__quantidade')  # Multiplicar pela quantidade produzida
         ).aggregate(total_material_usado=Sum('material_usado'))

    # Soma da quantidade de material usada nas produções de roupas
        estoque_producao = producao_estoque['total_material_usado'] or 0

    # Calcula o estoque atual: entradas - saídas
        return estoque_movimentacao - estoque_producao

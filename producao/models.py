from django.db import models
from roupa.models import Roupa

# Create your models here.
class Producao(models.Model):
    roupa = models.ForeignKey(Roupa, on_delete= models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
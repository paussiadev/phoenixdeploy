from django import forms
from movimentacao.models import Movimentacao

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = '__all__'
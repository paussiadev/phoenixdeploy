from django import forms
from producao.models import Producao

class ProducaoForm(forms.ModelForm):
    class Meta:
        model = Producao
        fields = '__all__'

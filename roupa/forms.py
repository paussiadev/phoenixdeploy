from django import forms
from roupa.models import Roupa, RoupaMaterial

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'descricao', 'imagem', 'materiais']
        widgets = {
            'materiais': forms.CheckboxSelectMultiple(), 
        }

class RoupaMaterialForm(forms.ModelForm):
    class Meta:
        model = RoupaMaterial
        fields = ['roupa', 'material', 'quantidade']
from django import forms
from material.models import Material
from roupa.models import Roupa, RoupaMaterial

class RoupaForm(forms.ModelForm):
    materiais = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Roupa
        fields = ['nome', 'descricao', 'imagem', 'materiais']

class RoupaMaterialForm(forms.ModelForm):
    class Meta:
        model = RoupaMaterial
        fields = ['material', 'quantidade']

RoupaMaterialFormSet = forms.inlineformset_factory(
    Roupa,  # Modelo pai
    RoupaMaterial,  # Modelo filho (relacionamento com quantidade)
    fields=['material', 'quantidade'],  # Campos a serem exibidos no form
    extra=1,  # Quantidade de formulários extras exibidos inicialmente
    can_delete=True  # Permite remover materiais
)
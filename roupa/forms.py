from django import forms
from material.models import Material
from roupa.models import Roupa, RoupaMaterial

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'descricao', 'imagem']

class RoupaMaterialForm(forms.ModelForm):
    class Meta:
        model = RoupaMaterial
        fields = ['material', 'quantidade']

RoupaMaterialFormSet = forms.inlineformset_factory(
    Roupa,
    RoupaMaterial,
    form=RoupaMaterialForm,
    fields=['material', 'quantidade'],
    extra=1,
    can_delete=True
)

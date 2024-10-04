from django import forms
from material.models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

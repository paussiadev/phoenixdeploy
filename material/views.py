from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from material.forms import MaterialForm
from material.models import Material
from django.contrib.auth.mixins import LoginRequiredMixin

class MaterialListView(LoginRequiredMixin, ListView):
    model= Material
    context_object_name = 'materiais'
    template_name = 'material_list_view.html'

    def get_context_data(self, **kwargs):
        # Primeiro, chamamos o método original para obter o contexto padrão
        context = super().get_context_data(**kwargs)
        
        # Calculamos o estoque de cada material
        for material in context['materiais']:
            material.estoque_atual = material.estoque_atual()  # Método que criamos na model

        # Retornamos o contexto com o estoque adicionado
        return context
    
class MaterialDetailView(LoginRequiredMixin,DetailView):
    model= Material
    template_name = 'material_detail_view.html'

class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material_form.html'
    success_url = reverse_lazy('material_list')

class MaterialUpdateView(LoginRequiredMixin, UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material_form.html'
    success_url = reverse_lazy('material_list')


class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = Material
    success_url = reverse_lazy('material_list')
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from material.forms import MaterialForm
from material.models import Material

class MaterialListView(ListView):
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
    
class MaterialDetailView(DetailView):
    model= Material
    template_name = 'material_detail_view.html'

class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material_form.html'
    success_url = reverse_lazy('material_list')

class MaterialUpdateView(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material_form.html'
    success_url = reverse_lazy('material_list')


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('material_list')
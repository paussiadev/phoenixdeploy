from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from material.forms import MaterialForm
from material.models import Material

class MaterialListView(ListView):
    model= Material
    template_name = 'material_list_view.html'
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
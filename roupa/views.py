from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from roupa.forms import RoupaForm, RoupaMaterialForm
from roupa.models import Roupa, RoupaMaterial

# Create your views here.
class RoupaListView(ListView):
    model= Roupa
    template_name = 'roupa_list_view.html'

class RoupaDetailView(DetailView):
    model= Roupa
    template_name = 'roupa_detail_view.html'

class RoupaCreateView(CreateView):
    model = Roupa
    form_class = RoupaForm
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('roupa_list')

class RoupaMaterialCreateView(CreateView):
    model = RoupaMaterial
    form_class = RoupaMaterialForm
    template_name = 'roupa_material_form.html'
    success_url = reverse_lazy('lista_roupas')  

class RoupaUpdateView(UpdateView):
    model = Roupa
    form_class = RoupaForm
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('roupa_list')

class RoupaDeleteView(DeleteView):
    model = Roupa
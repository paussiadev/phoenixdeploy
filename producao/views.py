from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from producao.forms import ProducaoForm
from producao.models import Producao

# Create your views here.
class ProducaoListView(ListView):
    model= Producao
    template_name = 'producao_list_view.html'

class ProducaoDetailView(DetailView):
    model= Producao
    template_name = 'producao_detail_view.html'

class ProducaoCreateView(CreateView):
    model = Producao
    form_class = ProducaoForm
    template_name = 'producao_form.html'
    success_url = reverse_lazy('producao_list')

class ProducaoUpdateView(UpdateView):
    model = Producao
    form_class = ProducaoForm
    template_name = 'producao_form.html'
    success_url = reverse_lazy('producao_list')

class ProducaoDeleteView(DeleteView):
    model = Producao
    success_url = reverse_lazy('producao_list')
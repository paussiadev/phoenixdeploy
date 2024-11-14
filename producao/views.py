from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from producao.forms import ProducaoForm
from producao.models import Producao
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProducaoListView(LoginRequiredMixin, ListView):
    model= Producao
    template_name = 'producao_list_view.html'

class ProducaoDetailView(LoginRequiredMixin, DetailView):
    model= Producao
    template_name = 'producao_detail_view.html'

class ProducaoCreateView(LoginRequiredMixin, CreateView):
    model = Producao
    form_class = ProducaoForm
    template_name = 'producao_form.html'
    success_url = reverse_lazy('producao_list')

class ProducaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producao
    form_class = ProducaoForm
    template_name = 'producao_form.html'
    success_url = reverse_lazy('producao_list')

class ProducaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producao
    success_url = reverse_lazy('producao_list')
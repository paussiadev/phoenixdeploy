from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from movimentacao.forms import MovimentacaoForm
from movimentacao.models import Movimentacao
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MovimentacaoListView(LoginRequiredMixin, ListView):
    model= Movimentacao
    template_name = 'movimentacao_list_view.html'

class MovimentacaoDetailView(LoginRequiredMixin, DetailView):
    model= Movimentacao
    template_name = 'movimentacao_detail_view.html'

class MovimentacaoCreateView(LoginRequiredMixin, CreateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')

class MovimentacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')

class MovimentacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Movimentacao
    success_url = reverse_lazy('movimentacao_list')
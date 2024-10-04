from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from movimentacao.forms import MovimentacaoForm
from movimentacao.models import Movimentacao

# Create your views here.
class MovimentacaoListView(ListView):
    model= Movimentacao
    template_name = 'movimentacao_list_view.html'

class MovimentacaoDetailView(DetailView):
    model= Movimentacao
    template_name = 'movimentacao_detail_view.html'

class MovimentacaoCreateView(CreateView):
    model = Movimentacao
    template_name = 'movimentacao_form.html'
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')

class MovimentacaoUpdateView(UpdateView):
    model = Movimentacao
    template_name = 'movimentacao_form.html'

class MovimentacaoDeleteView(DeleteView):
    model = Movimentacao
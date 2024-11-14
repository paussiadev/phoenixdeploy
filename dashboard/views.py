from typing import Any
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from roupa.models import Roupa
from producao.models import Producao
from movimentacao.models import Movimentacao
from material.models import Material
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(LoginRequiredMixin, TemplateView):
    login_url = 'login' 
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data()

        ultimas_roupas = Roupa.objects.order_by('-id')[:5]
        context['ultimas_roupas'] = ultimas_roupas

        ultimas_producao = Producao.objects.order_by('-id')[:5]
        context['ultimas_producao'] = ultimas_producao

        ultimas_movimentacao = Movimentacao.objects.order_by('-id')[:5]
        context['ultimas_movimentacao'] = ultimas_movimentacao

        ultimos_materias = Material.objects.order_by('-id')[:5]
        context['ultimos_materiais'] = ultimos_materias 
        
        return context
    
class CustomLoginView(LoginView):
    template_name = 'login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('dashboard')  

    def get_success_url(self):
        return self.success_url or super().get_success_url()

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')
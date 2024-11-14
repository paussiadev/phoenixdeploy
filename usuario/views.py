from pyexpat.errors import messages
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'usuario/profile_detail.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user  # Retorna o usuário logado


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'usuario/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user 

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/password_change.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Senha alterada com sucesso!')
        return super().form_valid(form)
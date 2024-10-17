from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserUpdateForm


class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'usuario/profile_detail.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user  # Retorna o usuário logado


class UserProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'usuario/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user 
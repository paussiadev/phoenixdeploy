from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from roupa.forms import RoupaForm, RoupaMaterialForm, RoupaMaterialFormSet
from roupa.models import Roupa
from django.contrib.auth.mixins import LoginRequiredMixin


class RoupaListView(LoginRequiredMixin, ListView):
    model = Roupa
    template_name = 'roupa_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roupas = context['object_list']
        for roupa in roupas:
            roupa.valor_producao = roupa.valor_producao()
        return context

class RoupaDetailView(LoginRequiredMixin, DetailView):
    model = Roupa
    context_object_name = 'roupa'
    template_name = 'roupa_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roupa = self.object
        context['valor_producao'] = roupa.valor_producao()
        context['materiais'] =  self.object.roupamaterial_set.select_related('material').all()
        return context
    
class RoupaCreateView(LoginRequiredMixin, CreateView):
    model = Roupa
    form_class = RoupaForm
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('roupa_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            # Passa uma instância vazia de Roupa para o formset ao postar dados
            data['material_formset'] = RoupaMaterialFormSet(self.request.POST)
        else:
            # Inicializa o formset vazio para requisições GET
            data['material_formset'] = RoupaMaterialFormSet()
        return data

    def form_valid(self, form):
        # Salva a instância da roupa antes de lidar com o formset
        self.object = form.save()

        # Associa a instância da roupa ao formset
        context = self.get_context_data()
        material_formset = context['material_formset']
        material_formset.instance = self.object

        if material_formset.is_valid():
            material_formset.save()
            return redirect(self.success_url)
        else:
            # Caso o formset seja inválido, renderiza o formulário com erros
            return self.form_invalid(form)

class RoupaUpdateView(LoginRequiredMixin, UpdateView):
    model = Roupa
    form_class = RoupaForm
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('roupa_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['material_formset'] = RoupaMaterialFormSet(self.request.POST, instance=self.object)
        else:
            data['material_formset'] = RoupaMaterialFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        material_formset = context['material_formset']

        if form.is_valid() and material_formset.is_valid():
            # Atualiza a roupa primeiro
            self.object = form.save(commit=False)
            self.object.save()

            # Atualiza os materiais
            material_formset.instance = self.object
            material_formset.save()

            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        return self.render_to_response(context)

class RoupaDeleteView(LoginRequiredMixin, DeleteView):
    model = Roupa
    success_url = reverse_lazy('roupa_list')

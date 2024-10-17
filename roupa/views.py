from pyexpat.errors import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from roupa.forms import RoupaForm, RoupaMaterialForm, RoupaMaterialFormSet
from roupa.models import Roupa, RoupaMaterial

# Create your views here.
class RoupaListView(ListView):
    model= Roupa
    template_name = 'roupa_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roupas = context['object_list']
        
        for roupa in roupas:
            roupa.valor_producao = roupa.valor_producao()
        
        return context

 

class RoupaDetailView(DetailView):
    model= Roupa
    context_object_name = 'roupa'  
    template_name = 'roupa_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        roupa = self.object
        
        context['valor_producao'] = roupa.valor_producao()
        
        return context

class RoupaCreateView(CreateView):
    model = Roupa
    fields = ['nome', 'descricao', 'imagem']
    template_name = 'roupa_form.html'
    success_url = reverse_lazy('roupa_list')

    # Sobrescrevendo o método para incluir o formset
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['material_formset'] = RoupaMaterialFormSet(self.request.POST)
        else:
            data['material_formset'] = RoupaMaterialFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        material_formset = context['material_formset']
        if material_formset.is_valid():
            self.object = form.save()
            material_formset.instance = self.object
            material_formset.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

class RoupaMaterialCreateView(CreateView):
    model = RoupaMaterial
    form_class = RoupaMaterialForm
    template_name = 'roupa_material_form.html'
    success_url = reverse_lazy('lista_roupas')

    def post(self, request, *args, **kwargs):
        roupa_form = self.get_form()
        material_forms = []

        if roupa_form.is_valid():
            roupa = roupa_form.save()
            materials = request.POST.getlist('materiais')

            for material in materials:
                quantidade = request.POST.get(f'quantidade_{material}')
                if quantidade:
                    material_forms.append(RoupaMaterial(roupa=roupa, material_id=material, quantidade=quantidade))

            RoupaMaterial.objects.bulk_create(material_forms)
            messages.success(request, "Roupa criada com sucesso!")
            return redirect(self.get_success_url())
        
        return self.form_invalid(roupa_form)

class RoupaUpdateView(UpdateView):
    model = Roupa
    fields = ['nome', 'descricao', 'imagem']
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
        if material_formset.is_valid():
            self.object = form.save()
            material_formset.instance = self.object
            material_formset.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

class RoupaDeleteView(DeleteView):
    model = Roupa
    success_url = reverse_lazy('roupa_list')
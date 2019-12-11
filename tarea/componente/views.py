from django.shortcuts import render
from .models import Componente
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class ComponenteListView(ListView):
    model = Componente

class ComponenteCreateView(CreateView):
    model = Componente
    fields = '__all__'

class ComponenteUpdateView(UpdateView):
    model = Componente
    fields = '__all__'
    template_name_suffix = '_update_form'

class ComponenteDeleteView(DeleteView):
    model = Componente
    success_url = reverse_lazy('componente:componente-list')
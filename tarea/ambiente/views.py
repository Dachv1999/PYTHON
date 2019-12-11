from django.shortcuts import render
from .models import Ambiente
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class AmbienteListView(ListView):
    model = Ambiente

class AmbienteCreateView(CreateView):
    model = Ambiente
    fields = '__all__'

class AmbienteUpdateView(UpdateView):
    model = Ambiente
    fields = '__all__'
    template_name_suffix = '_update_form'

class AmbienteDeleteView(DeleteView):
    model = Ambiente
    success_url = reverse_lazy('ambiente:ambiente-list')

from django.shortcuts import render

from django.views.generic import ListView

# Models
from .models import Autor

# Create your views here.

class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'
    # paginate_by = 10
    # queryset = Autor.objects.all()
    def get_queryset(self):
        return Autor.objects.all()
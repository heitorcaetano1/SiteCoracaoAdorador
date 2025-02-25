from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Produto, Categoria


class ListaProdutoView(TemplateView):
    template_name = 'lista_produto.html'

    def get_context_data(self, **kwargs):
        context = super(ListaProdutoView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all().order_by('?')
        return context


class DetalheProdutoView(DetailView):
    model = Produto
    template_name = 'detalhe_produto.html'
    context_object_name = 'produto'

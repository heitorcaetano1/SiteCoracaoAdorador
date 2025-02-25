from django.contrib import admin
from django.utils.html import format_html

from .models import Produto, Categoria, Variacao


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'imagem', 'estoque', 'data_criacao', 'categoria')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')


@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'nome', 'preco', 'estoque')

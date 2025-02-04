from django.contrib import admin
from .models import Cliente, Endereco, Pedido, ItemPedido


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'cpf_cnpj')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    lst_display = ('logradouro', 'cidade', 'estado', 'cep')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'status', 'valor_total')


@admin.register(ItemPedido)
class ItemPedidoAdmin():
    list_display = ('pedido', 'produto', 'quantidade', 'preco_unitario')

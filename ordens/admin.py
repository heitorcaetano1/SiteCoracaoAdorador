from django.contrib import admin
from .models import Pedido, ItemPedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_pedido', 'status', 'valor_total', 'endereco_entrega', 'forma_pagamento')

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display =  ('pedido', 'produto', 'quantidade', 'preco_unitario')

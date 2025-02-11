from django.contrib import admin
from .models import Pagamento, Transacao


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'metodo_pagamento', 'status_pagamento', 'data_pagamento', 'valor_pago', 'transacao_id')


@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('pagamento', 'gateway_data')

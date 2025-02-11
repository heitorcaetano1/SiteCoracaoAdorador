from django.db import models
from ordens.models import Pedido


class Pagamento(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='pagamento')
    metodo_pagamento = models.CharField(max_length=50, choices=[('cartao', 'Cartão de Crédito'), ('boleto', 'Boleto Bancário'), ('pix', 'Pix'), ('debito', 'Cartão de Débito')])
    status_pagamento = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('aprovado', 'Aprovado'), ('cancelado', 'Cancelado')], default='pendente')
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    transacao_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.pedido, self.status_pagamento, self.transacao_id

class Transacao(models.Model):
    pagamento = models.OneToOneField(Pagamento, on_delete=models.CASCADE, related_name='transacao')
    gateway_data = models.JSONField(blank=True, null=True)

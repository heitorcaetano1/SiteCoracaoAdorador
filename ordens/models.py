from django.db import models
from cliente.models import Cliente
from produtos.models import Produto


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ordens_pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('P', 'Pendente'), ('A', 'Aprovado'), ('C', 'Cancelado'), ('E', 'Enviado')], default='P')
    valor_total = models.DecimalField(max_digits=20, decimal_places=2)
    endereco_entrega = models.ForeignKey('Endereco', on_delete=models.SET_NULL, null=True, blank=True, related_name='endereco_entregas')
    forma_pagamento = models.CharField(max_length=50)

    def __str__(self):
        return self.cliente, self.status


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='ordens_itens_pedidos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='ordens_itens_pedido')
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='enderecos')
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2, choices=[('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro')])
    cep = models.CharField(max_length=9)
    principal = models.BooleanField(default=False)

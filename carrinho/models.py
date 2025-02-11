from django.db import models
from cliente.models import Cliente
from produtos.models import Produto


class Carrinho(models.Model):
    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='carrinho')
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

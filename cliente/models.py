from django.db import models
from produtos.models import Produto


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    sobrenome = models.CharField(max_length=100, verbose_name='Sobrenome')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    cpf_cnpj = models.CharField(max_length=14, unique=True, verbose_name='CPF/CNPJ')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], null=True, verbose_name='Gêneros')
    newsletter = models.BooleanField(default=False, verbose_name='Receber Newsletter')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


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


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('P', 'Pendente'), ('A', 'Aprovado'), ('C', 'Cancelado')], default='P')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

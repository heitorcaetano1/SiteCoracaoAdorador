from django.db import models
from stdimage import StdImageField


class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    imagem = StdImageField(upload_to='produtos/imagens/', verbose_name='Imagem do Produto', variations={'thumb' : {'width': 480, 'height' : 480, 'crop': True}})
    estoque = models.PositiveIntegerField(default=0, verbose_name='Estoque')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Categoria')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='variacoes')
    nome = models.CharField(max_length=50, verbose_name='Nome da Variação')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    estoque = models.PositiveIntegerField(default=0, verbose_name='Estoque')

    def __str__(self):
        return self.nome

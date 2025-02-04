from django.contrib.auth.models import User
from django.db import models

class Configuracao(models.Model):
    nome_site = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)
    endereco = models.TextField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    redes_sociais = models.JSONField(default=dict, blank=True, verbose_name='Redes Sociais')
    horario_atendimento = models.CharField(max_length=100, blank=True, verbose_name='Horário de Funcionamento')

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'


class PaginaEstatica(models.Model):
    """Se você tiver páginas com conteúdo que não muda frequentemente, como "Sobre nós", "Contato" ou
    "Política de privacidade", você pode criar um modelo para armazenar o conteúdo dessas páginas.
    Isso permite que você edite o conteúdo diretamente
    do painel administrativo, sem precisar modificar os templates."""
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo


class Log(models.Model):
    """Para registrar eventos importantes, como logins de usuários, erros do sistema, etc."""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()


class Pagamento(models.Model):
    '''Modelo para armazenar as configurações de Pagamento'''
    gateway = models.CharField(max_length=50, choices=[('paypal', 'PayPal'), ('pagseguro', 'PagSeguro'), ('stripe', 'Stripe')], default='paypal', verbose_name='Gateway de pagamento')
    chave_api = models.CharField(max_length=255, verbose_name='Chave API')
    modo_teste = models.BooleanField(default=True, verbose_name='Modo de Teste')


class EmailConfig(models.Model):
    host = models.CharField(max_length=100, verbose_name='Host')
    port = models.IntegerField(verbose_name='Porta')
    username = models.EmailField(verbose_name='Usuário')
    password = models.CharField(max_length=100, verbose_name='Senha')
    email_from = models.EmailField(verbose_name='E-mail de Remessa')

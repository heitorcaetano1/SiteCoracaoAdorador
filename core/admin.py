from django.contrib import admin
from .models import Configuracao, PaginaEstatica, Pagamento, EmailConfig, Log


@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('nome_site', 'email', 'telefone')


@admin.register(PaginaEstatica)
class PaginaEstaticaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug')
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('gateway', 'modo_teste')


@admin.register(EmailConfig)
class EmailConfigAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'email_from')


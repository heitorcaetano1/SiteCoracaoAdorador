from django.contrib import admin
from .models import Configuracao, PaginaEstatica, Pagamento, EmailConfig, Log


@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('nome_site', 'email', 'telefone')
    readonly_fields = ('id')

@admin.register(PaginaEstatica)
class PaginaEstaticaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug')
    prepopulated_fields = {'slug': ('titutlo',)}
    readonly_fields = ('id')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('gateway', 'modo_teste')
    readonly_fields = ('id')

@admin.register(EmailConfig)
class EmailConfigAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'email_from')
    readonly_fields = ('id')

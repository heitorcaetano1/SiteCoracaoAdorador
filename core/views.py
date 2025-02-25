from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Configuracao, PaginaEstatica


def home(request):
    return render(request, 'index.html')

def about(request):
    pagina = PaginaEstatica.objects.frist()
    return render(request, 'about.html', {'pagina': pagina})

def contact(request):
    if request.method == 'POST':
        pass
    return render(request, 'contato.html')

def privacidade(request):
    return render(request, 'privacidade.html')

def terms(request):
    return render(request, 'terms.html')

class TabelaMedidasView(TemplateView):
    template_name = 'tabela_medidas.html'


class CuidadosPecaView(TemplateView):
    template_name = 'cuidados_peca.html'

from django.shortcuts import render
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

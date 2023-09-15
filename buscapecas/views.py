from django.shortcuts import render
from buscapecas.buscar_produto import pesquisar_produto

def home(request):

    context = {
        'titulo' : 'Home',
    }

    return render(request, 'index.html', context)

def pesquisa(request):

    if request.method == 'POST':

        form_data = request.POST

        pesquisa = form_data.get('search')

        pesquisa.replace('ç', 'c')

        if pesquisa.strip() == "":
            return render(request, 'index.html')

        produtos = pesquisar_produto(pesquisa)

        context = {
            'titulo' : pesquisa,
            'produtos' : produtos
        }

        # Faça algo com o resultado, se necessário
        return render(request, 'pesquisa.html', context)
    else:
        return render(request, 'index.html')
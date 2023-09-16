import requests
from bs4 import BeautifulSoup
from operator import itemgetter

def pesquisar_produto(item):
    lista_produtos = []
    url_base = 'https://lista.mercadolivre.com.br/'

    produto_nome = item

    response = requests.get(url_base + produto_nome)

    if response.status_code == 200:
        site = BeautifulSoup(response.text, 'html.parser')

        produtos = site.findAll('div', class_='andes-card')

        for produto in produtos:
            try:
                foto = produto.find('img', class_='shops__image-element')
                titulo = produto.find('h2', class_='ui-search-item__title')
                link = produto.find('a', class_='ui-search-link')

                real = produto.find('span', class_='andes-money-amount__fraction')
                centavos = produto.find('span', class_='andes-money-amount__cents')

                if (centavos):
                    valor = real.text + ',' + centavos.text
                else:
                    valor = real.text

                lista_produtos.append({
                    "image": f"{foto['data-src']}",
                    "title": f"{titulo.text}",
                    "link": f"{link['href']}",
                    "price": f"{valor}",
                    "store" : 1,
                })
                
            except AttributeError:
                break

            except TypeError:
                break
            
    return sorted(lista_produtos, key=itemgetter('price'))
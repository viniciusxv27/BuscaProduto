import requests
from bs4 import BeautifulSoup
from operator import itemgetter

def pesquisar_produto(produto_nome):
    lista_produtos = []
    url_base1 = 'https://lista.mercadolivre.com.br/'
    url_base2 = 'https://www.amazon.com.br/s?k='
    url_base3 = 'https://www.magazineluiza.com.br/busca/'
    
    response1 = requests.get(url_base1 + produto_nome)

    if response1.status_code == 200:
        site = BeautifulSoup(response1.text, 'html.parser')

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

    response2 = requests.get(url_base2 + produto_nome)

    if response2.status_code == 200:
        site = BeautifulSoup(response2.text, 'html.parser')

        produtos = site.findAll('div', class_='s-asin')

        for produto in produtos:
            try:
                foto = produto.find('img', class_='s-image')
                titulo = produto.find('span', class_='a-text-normal')
                link = produto.find('a', class_='a-link-normal')

                real = produto.find('span', class_='a-price-whole')
                centavos = produto.find('span', class_='a-price-fraction')

                if (centavos):
                    valor = real.text + centavos.text
                else:
                    valor = real.text

                lista_produtos.append({
                    "image": f"{foto['src']}",
                    "title": f"{titulo.text}",
                    "link": f"{link['href']}",
                    "price": f"{valor}",
                    "store" : 2,
                })
                
            except AttributeError:
                break

            except TypeError:
                break

    response3 = requests.get(url_base3 + produto_nome)

    if response3.status_code == 200:
        site = BeautifulSoup(response3.text, 'html.parser')

        produtos = site.findAll('li', class_='sc-dxlmjS')

        for produto in produtos:
            try:
                foto = produto.find('img', class_='sc-dtInlm')
                titulo = produto.find('h2', class_='sc-ijtseF')
                link = produto.find('a', class_='sc-jRBLiq')

                valor = produto.find('p', class_='sc-eXsaLi')

                lista_produtos.append({
                    "image": f"{foto['src']}",
                    "title": f"{titulo.text}",
                    "link": f"https://www.magazineluiza.com.br{link['href']}",
                    "price": f"{valor.text}",
                    "store" : 3,
                })
                
            except AttributeError:
                break

            except TypeError:
                break

    lista_produtos = sorted(lista_produtos, key=itemgetter('price'))

    return lista_produtos
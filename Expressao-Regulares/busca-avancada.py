import re

def busca_avancada():
    print('Digite algo para buscar!')
    texto = 'Digite algo para buscar!'

    valor = raw_input()
    resultado = re.findall('([' + valor + ' ]\w+)', texto)

    print resultado
busca_avancada()
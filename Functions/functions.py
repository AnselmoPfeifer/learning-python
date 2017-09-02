convite = 'Meu Nome Completo'
parte1 = convite[0:3]
parte2 = convite[4:8]
parte3 = convite[9:17]

print parte1
print parte2
print parte3

tamanho = len(convite)
print tamanho

sobrenome = convite[tamanho-8:tamanho]
print sobrenome

posicao_final = tamanho
posicao_inicial = posicao_final-13

parte2 = convite[posicao_inicial:posicao_final]
print parte2

def gera_nome_convite(nome):
    nome_completo = nome
    tamanho = len(nome_completo)
    posicao_final = tamanho
    posicao_inicial = posicao_final - 13

    sobrenomes = nome_completo[posicao_inicial:posicao_final]
    print '%s' % (sobrenomes)

gera_nome_convite('Meu Nome Completo')

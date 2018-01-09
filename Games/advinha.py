from random import randint

print ('Bem Vindo')

sorteado = randint(1, 100)
chute = 0

while chute != sorteado:
    chute = int(input ('Tentaiva: '))
    if chute == sorteado:
        print ('Ganhou')
    else:
        if chute > sorteado:
            print('Chute alto')
        else:
            print('Chute Baixo')
print('Fim de jogo')

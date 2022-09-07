from random import randint
computador=randint(0,10)
palpites=0
print('Olá, sou seu computador, bora jogar?')
print('Tente advinhar qual é o númro entre 0 á 10 que estou pensando.')
jogador=int(input('Digite aqui o seu número:'))
acertar=False
while not acertar:
    jogador=int(input('Huum, tente novamente:'))
    palpites=palpites+1
    if jogador==computador:
        acertar=True
        print('Acertoouu!')
    else:
        if jogador > computador:
            print('Menoos ...')
        if jogador < computador:
            print('Maaais ...')
print('Parabéns! Você acertou depois de {} palpites.'.format(palpites))



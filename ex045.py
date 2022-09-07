import random
print('Bora jogar?!')
print('[1] PAPEL')
print('[2] PEDRA')
print('[3] TESOURA')
opcao=int(input('Digite aqui a sua opção:'))
lista=[1,2,3]
computador=random.choice(lista)
print('Computador: O meu número escolhido foi {}!'.format(computador))
if computador == 1 and opcao == 2 or computador==3 and opcao ==1 or computador==2 and opcao==3:
    print('Você perdeu jogador MUHAHAHA!')
elif opcao==1 and computador==2 or opcao==3 and computador==1 or opcao==2 and computador==3:
    print('Você ganhou jogador!')
else:
    print('Empataram!')








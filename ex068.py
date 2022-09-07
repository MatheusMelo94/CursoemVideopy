from random import randint
v=0
print('Olá, sou o seu computador! bora jogar PAR OU IMPAR?')
while True:
    jogador = int(input('Digite aqui o seu número:'))
    computador = randint(0, 10)
    total = computador + jogador
    tipo='PI'
    opcao = str(input('PAR OU IMPAR?')).upper().strip()[0]
    print(f'Você colocou {jogador} e o computador {computador}. Total de {total}.')
    if opcao=='P':
        if total%2==0:
            print('Você VENCEU!')
            v=v+1
        if total%2==1:
            print('Você PERDEU!')
            break
    elif opcao=='I':
        if total%2==1:
            print('Você GANHOU!')
            v=v+1
        if total%2==0:
            print('Você PERDEU!')
            break
print(f'Você venceu {v} vezes o computador!')











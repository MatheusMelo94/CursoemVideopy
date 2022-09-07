n1=int(input('Digite aqui o primeiro valor:'))
n2=int(input('Digite aqui o segundo valor:'))
soma=0
opcao=0
while opcao !=5:
    print('[1] SOMA')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    opcao=int(input('O que você deseja fazer com esses valores?'))
    if opcao==1:
        soma=n1+n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    elif opcao==2:
        produto=n1*n2
        print('Os numeros {} e {} multiplicados é {}'.format(n1,n2,produto))
    elif opcao == 3:
        if n1>n2:
            maior=n1
        if n2>n1:
            maior=n2
        print('O maior valor entre {} e {} é {}'.format(n1,n2,maior))
    elif opcao==4:
        n1=int(input('Digite o primeiro novo valor:'))
        n2=int(input('Digite o segundo novo valor:'))
    elif opcao==5:
        print('Finalizando programa ...')
print('Programa finalizado com sucesso!')



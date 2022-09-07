n=int(input('Digite aqui o seu número ou aperte 999 para PARAR:'))
soma=0
cont=0
while n!=999:
    soma=soma+n
    cont=cont+1
    n = int(input('Digite aqui o seu nùmero:'))
    if n==999:
        print('Finalizando programaa ..')
print('O total de numero digitados foi de {} e a soma entre eles foi de {}.'.format(cont,soma))


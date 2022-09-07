soma=maior=menor=cont=media=0
resp='S'
while resp in 'S':
    n=int(input('Digite aqui o número:'))
    soma=soma+n
    cont=cont+1
    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resp=str(input('Deseja continuar [S/N]:')).strip().upper()[0]
media=soma/cont
print('A soma de todos os números digitados foi {}.'.format(soma))
print('A média entre todos os números é de {}.'.format(media))
print('O maior número é {} e o menor é {}.'.format(maior,menor))





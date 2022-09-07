soma=0
for c in range (0,6):
    n=int(input('Digite um valor:'))
    if n%2==0:
        soma=soma+n
print('A soma de todos os numeros pares é de {}'.format(soma))

soma=0
cont=0
while True:
    num=int(input('Digite aqui o número (999 para PARAR):'))
    if num==999:
        break
    soma=soma+num
    cont=cont+1
print(f'A quantidade de número digitados foram de {cont}.')
print(f'A soma total dos valores digitados foi de {soma}.')



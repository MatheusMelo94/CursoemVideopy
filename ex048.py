soma=0
cont=0
for c in range (1,500+1,2):
    if c%3==0:
        soma=soma+c
        cont+=1
        print(c,end=' ')
print('\nA soma entre os {} números, tem o total de {}.'.format(cont,soma))

primeiro=int(input('Digite aqui o primeiro termo:'))
razao=int(input('Digite aqui a razao:'))
termo=primeiro
cont=1
total=0
mais=10
while mais!=0:
    total=total+mais
    while cont<=total:
        print('{}'.format(termo),end='--')
        termo=termo+razao
        cont=cont+1
    print('PAUSA')
    mais=int(input('Quantos termos mais você gostaria de mostrar?'))
print('Progressão finalizada com {} termos.'.format(total))


print('GERADOR DE PA')
print('--*--'*10)
primeiro=int(input('Digite aqui o primeiro termo: '))
razao=int(input('Razão da PA: '))
termo= primeiro
cont=1
while cont<=19:
    print('{}'.format(termo), end='--')
    termo=termo+razao
    cont=cont+1
print('FIM!')


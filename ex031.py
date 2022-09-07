dist=int(input('Digite aqui a distância da viagem em km:'))
preço=dist*0.50
preço2=dist*0.45
if dist<200:
    print('Você deverá pagar {:.2f} reais'.format(preço))
else:
    ('Você deverá pagar {.:2f} reais'.format(preço2))
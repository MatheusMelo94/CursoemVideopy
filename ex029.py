velocidade=int(input('Digite aqui a velocidade do carro:'))
multa=(velocidade-80)*7
if velocidade>80:
    print('Você foi multado! Valor á pagar {} reais'.format(multa))
else:
    print('Carro sem multa!')
from random import randint
print('Olá! Vou pensar em um número de 0 a 5 e você tera que acertar!')
numero=int(input('Digite aqui o seu número:'))
escolhido=randint(0,5)
if numero ==escolhido:
    print('Parabéns! você acertou!')
else:
    print('OHOH Tente novemente!')
print('O número que eu pensei foi o {}'.format(escolhido))

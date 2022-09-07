numero = int(input('Digite aqui o seu número:'))
u= numero // 1 % 10
d=numero // 10 % 10
c=numero // 100 % 10
m=numero // 1000 % 10
print('A unidade seria: {}'.format(u))
print('A dezena seria: {}'.format(d))
print('A centena seria: {}'.format(c))
print('O milhar seria: {}'.format(m))



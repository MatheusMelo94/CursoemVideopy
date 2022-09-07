print('--*--'*10)
print('Sequência de Fibonacci!')
t1=0
t2=1
n=int(input('Digite aqui a o seu número e veja a sequência:'))
cont=3
print('{}-{}'.format(t1,t2),end='-')
while cont<=n:
    t3=t1+t2
    print(t3, end='-')
    t1=t2
    t2=t3
    cont=cont+1
print('fim')


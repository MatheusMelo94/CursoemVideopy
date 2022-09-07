m1=float(input('Digite aqui a primeira medida:'))
m2=float(input('Digite aqui a segunda medida:'))
m3=float(input('Digite aqui a terceira medida:'))
if m1+m2>m3:
    print('As medidas formaram um triângulo' , end=' ')
    if m1==m2==m3:
        print('EQUILÁTERO!')
    elif m1 != m2!= m3!=m1:
            print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os seguimentos não podem formar um triaângulo!')


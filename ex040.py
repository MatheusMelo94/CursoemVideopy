nota1=float(input('Digite aqui a primeira média:'))
nota2=float(input('Digite aqui a segunda média:'))
media=(nota1+nota2)/2
if media<5.0:
    print('REPROVADO!')
elif media >5 and media <7:
    print('RECUPERAÇÃO!')
elif media>=7.0:
    print('APROVADO!')


frase=str(input('Digite aqui a sua frase ou palavra:')).strip().upper()
separada=frase.split()
junto=''.join(frase)
invertido=junto[::-1]
if junto==invertido:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')

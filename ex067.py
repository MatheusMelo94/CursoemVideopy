while True:
    num=int(input('Digite aqui um número e veja a sua tabuada:'))
    if num<0:
        break
    for c in range(0,10):
        print(f'{num} x {c} = {num*c}')
print('Programa finalizado com sucesso!')







cont=0
menor=0
barato=''
total=0
cont1=0
while True:
    produto=str(input('Digite aqui o nome do produto:')).strip()
    preco=float(input('Digite aqui o valor do produto:'))
    cont1=cont1+1
    total=total+preco
    if preco>1000:
        cont=cont+1
    if cont1==1:
        menor=preco
        barato=produto
    else:
        if preco<menor:
            menor=preco
            barato=produto
    resp=' '
    while resp not in 'SN':
        resp=str(input('Você gostaria de continuar? S/N:')).upper().strip()
    if resp=='N':
        break
print(f'O total gasto nas compras foi de {total}')
print(f'Há {cont} produtos acima de 1.000BRL.')
print(f'O produto mais barato foi o {barato}.')


print('-*-'*30)
print('{:^30}'.format('-- BANCO MATHEUS MELO'))
valor=int(input('Qual é o valor você gostaria de sacar:'))
ced=50
totalced=0
total=valor
while True:
    if total>=ced:
        total=total-ced
        totalced=totalced+1
    else:
        if totalced>0:
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totaced=0
        if total==0:
            break








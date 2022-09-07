soma18=0
somah=0
somam20=0
while True:
    idade=int(input('Idade:'))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Sexo:')).strip().upper()
    if idade>=18:
        soma18=soma18+1
    if sexo=='M':
        somah=somah+1
    if sexo=='F' and idade<20:
        somam20=somam20+1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?')).upper().strip()
    if resp == 'N':
        break
print(f'A quantidade de pessoas maiores de 18 anos é {soma18}.')
print(f'Foram cadastrados {somah} homens.')
print(f'Há {somam20} mulheres com menos de 20 anos.')














ano_nascimento=int(input('Digite aqui o ano do atleta:'))
idade=2022-ano_nascimento
if idade<=9:
    print('MIRIM')
elif idade >9 and idade<=14:
    print('Categoria: INFANTIL!')
elif idade >14 and idade <=19:
    print('Categoria: JUNIOR!')
elif idade >19 and idade<=25:
    print('Categoria: SÊNIOR!')
else:
    print('Categoria: MASTER!')
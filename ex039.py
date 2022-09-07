ano_nascimento=int(input('Digite aqui o seu ano de nascimento:'))
idade=2022-ano_nascimento
alistamento=18

if idade<alistamento:
    print('Você ainda não presisa se alistar! A ainda faltam {} anos!'.format(alistamento-idade))
elif idade==alistamento:
    print('Você precisa se alistar esse ano!')
elif idade>alistamento:
    print('Você presisa se alistar! já se passaram {} anos!'.format(idade-alistamento))




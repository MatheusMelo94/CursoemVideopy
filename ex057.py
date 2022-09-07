sexo=str(input('Digite aqui o seu sexo [M/F]:')).strip().upper()
while sexo not in 'MFfm':
    print('Erro!')
    sexo=str(input('Digite novamente [M/F]:'))
print('Sexo {} validado com sucesso!'.format(sexo))

valor_casa=float(input('Qual é o valor da casa?'))
salario_comprador=float(input('Qual é o seu salário?'))
anos=int(input('Em quantos anos você vai pagar?'))
valor_prestacao=valor_casa/(anos*12)
exceder=salario_comprador*30/100

print('Você terá que pagar {:.2f} por mês'.format(valor_prestacao))

if valor_prestacao>exceder:
    print('Você não possui limite para o empréstimo!')
else:
    print('O seu crédito foi CONCEDIDO com sucesso!')



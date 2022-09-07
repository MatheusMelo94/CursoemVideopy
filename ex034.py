salario=float(input('Digite aqui o salário do funcionário:'))
aumento1=(salario*10/100)+salario
aumento2=(salario*15/100)+salario
if salario>1250:
    print('O seu salário obteve um aumento de 10%, totalizando um aumento de {:.2f} reais.'.format(aumento1))
if salario<1250:
    print('O seu salário obteve um aumento de 15%, totalizando {:.2f} reais.'.format(aumento2))

preço=float(input('Digite aqui o valor do produto:'))
print('[1] Á VISTA')
print('[2] Á VISTA NO CARTÃO')
print('[3] EM ATÉ 2X NO CARTÃO')
print('[4] EM 3X OU MAIS NO CARTÃO:')
opcao=int(input('Digite aqui a opção desejada:'))
if opcao==1:
    print('O valor a vista com um desconto de 10%, o produto ficaria {:.2f}BRL.'.format(preço-(preço*10/100)))
elif opcao ==2:
    print('O valor a vista no cartão com um desconto de 15%, o produto ficaria {:.2f}'.format(preço-(preço*15/100)))
elif opcao==3:
    print('Pagando em até 2x no cartão o preço ficaria normal: {}'.format(preço))
elif opcao==4:
    print('O preço ficaria {}'.format(preço + (preço*20/100)))


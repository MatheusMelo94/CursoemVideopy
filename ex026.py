frase=str(input('Digite aqui a sua frase:')).upper().strip()
print('A letra A, aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A, aparece a primeira vez na posicao {}'.format(frase.find('A')+1))
print('A letra A, aparece a última vez na posição {}'.format(frase.rfind('A')+1))

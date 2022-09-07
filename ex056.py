somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
totmulher20=0
for c in range (1,5):
    print('----- {}a pessoa -----'.format(c))
    nome=str(input('Digite aqui o seu nome:')).strip()
    idade=int(input('Digite aqui a sua idade:'))
    sexo=str(input('Digite aqui o seu sexo [M/F]:')).strip()
    somaidade=somaidade+idade
    if c==1 and sexo in 'Mn':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in'Mm' and idade >maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in'fF' and idade<20:
        totmulher20+=1
mediaidade=somaidade/4
print('A media de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))



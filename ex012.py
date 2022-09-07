p=float(input('Digite o preço: R$'))
pn=p-(p*5/100)
print('O preço que custava {}BRL, na promoção com desconto de 5% vai custar {:.2f}BRL'.format(p,pn))

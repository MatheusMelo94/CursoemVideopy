km=int(input('Quantos kilometros foram percorridos:'))
d=int(input('Quantos dias alugados:'))
dap=d*60
kmap=km*0.15
pagar=dap+kmap
print('O total a pagar é {:.2f}BRL'.format(pagar))

pt=int(input('Digite aqui o primeiro termo:'))
razao=int(input('Digite aqui a razão:'))
decima=pt+(10)*razao
for c in range (pt,decima,razao):
    print(c,end=' ')
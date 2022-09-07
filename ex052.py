soma=0
tot=0
n=int(input('Digite aqui um valor:'))
for c in range(1,n+1):
    if n%c==0:
        tot+=1
        print('\033[32m',end=' ')
    else:
        print('\033[031m',end=' ')
    print(c,end=' ')
if tot==2:
    print('\nEle é primo!')
else:
    print('\nEle não é primo!')



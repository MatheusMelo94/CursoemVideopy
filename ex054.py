from datetime import date
totmaior=0
totmenor=0
atual=date.today().year
for pess in range (0,8):
    nasc=int(input('Digite aqui a data de nascimento:'))
    idade = atual - nasc
    if idade>=21:
       totmaior+=1
    else:
        totmenor+=1
print('A quantidade de pessoa de maior é de {}'.format(totmaior))
print('A quantidade de pessoas de menor é {}'.format(totmenor))







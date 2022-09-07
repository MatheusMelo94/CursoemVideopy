''''import math
co=float(input('Digite aqui o comprimenro do cateto:'))
ca=float(input('Digite aqui o cateto adjacente:'))
h=(co**2+ca**2)**(1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(h)) '''

from math import hypot
co=float(input('Digite aqui o cateto oposto:'))
ca=float(input('Digite aqui o cateto adjacente:'))
h=(hypot(co,ca))
print('A hipotenusa vai medir {:.2f}'.format(h))
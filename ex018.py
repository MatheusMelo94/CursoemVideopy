from math import sin,cos,tan,radians
ang=float(input('Digite aqui o valor de angulo:'))
s=sin(radians(ang))
cos=cos(radians(ang))
tan=tan(radians(ang))
print('O angulo de {}, possui o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(ang,s,cos,tan))

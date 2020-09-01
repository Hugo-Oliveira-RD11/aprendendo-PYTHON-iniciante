from math import radians, sin, tan,cos
angulo = float(input('qual e o angulo que vc deseja :'))

seno = sin(radians(angulo))
tangencia = tan(radians(angulo))
cosseno = cos(radians(angulo))

print('o seno e {:.2f}\no cosseno e {:.2f}\na tangencia e {:.2f}'.format(seno, cosseno, tangencia))

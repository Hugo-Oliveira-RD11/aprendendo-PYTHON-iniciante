from math import hypot
cmenor = float(input('comprimento do cateto menor :'))
cmaior = float(input('comprimento do cateto maior :'))

h1 = hypot(cmenor, cmaior)

print ('a hipotenusa e {:.2f}'.format(h1))

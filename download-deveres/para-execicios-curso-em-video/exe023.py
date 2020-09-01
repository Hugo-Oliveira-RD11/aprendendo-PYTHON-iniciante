numero = int(input('digite um numero :'))

#não entendi a logica, revisar depois

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('a unidade do numero {} e {}'.format(numero,u))
print('a dezena e  {}\na centena e {}\no milhar e  {}'.format(d, c, m))

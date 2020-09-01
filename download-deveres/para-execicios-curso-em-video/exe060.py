multiplicar = 1
print('DIGITE UM NUMERO PARA EU SABER O FATORIAL DELE!')
n1 = int(input('digite um numero :'))
print('calculando {}!'.format(n1), end='')
while not n1 == 1:
    multiplicar *= n1
    n1 -= 1
print('o resultado é {}'.format(multiplicar))

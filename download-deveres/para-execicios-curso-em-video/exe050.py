soma = 0
for c in range(0, 6):
    n = int(input('digite um numero :'))
    if n % 2 == 0:
        soma = soma + n
print('a soma entre os numeros inpares e {}'.format(soma))

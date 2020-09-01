soma = 0
conta = 0
c = 0
while not c == 999:
    c = int(input('digite um valor : [ 999 para PARAR ] :'))
    conta += 1
    if c != 999:
        soma = (soma + c)
print('vc digitou {} numeros e a soma entre eles e {}'.format(conta - 1, soma))

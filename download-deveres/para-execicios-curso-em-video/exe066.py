conta = 0
soma = 0
valor = 0
while True:
    valor = int(input('digite um valor : (999 para PARAR)'))
    if valor == 999:
        break
    else:
        conta += 1
        soma += valor
print('au total foram {} numeros e a soma entre eles foi de {}'.format(conta, soma))

from time import sleep
maior = 0
menor = 100000000000000000000000000000000000000000000000000000000000
for kilo in range(1, 5+1):
    peso = float(input('peso da {}° pessoa :'.format(kilo)))
    sleep(0.1)
    if peso >= maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('o MAIOR peso lido foi de {:.2f}Kg\no MENOR peso lido foi de {:.2f}Kg'.format(maior, menor))

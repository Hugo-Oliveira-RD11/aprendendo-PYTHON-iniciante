from random import randint
'''numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

aleatorio = randint(numeros)
print(aleatorio)'''
conta = 0
for c in range(0, 5):
    conta += 1
    aleatorio = randint(0, 10)
    print(aleatorio, end=' ')
    if conta == 0:
        maior = aleatorio
        menor = aleatorio
    if conta != 0:
        if maior > aleatorio:
            maior == aleatorio
        elif menor < aleatorio:
            menor = aleatorio

print(f'o maior e {maior}\ne o menor e {menor}')

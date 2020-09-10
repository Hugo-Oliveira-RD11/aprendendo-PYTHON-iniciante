from time import sleep
nuns = (int(input('digite um numero :')),
int(input('digite outro numero :')),
int(input('digite o 3° numero :')),
int(input('digite o ultimo numero :')))
print('CARREGANDO...')
sleep(1)
print(f'vc digitou {nuns}')
nove = 0
tres = 0
par = 0
contem = 0
while True:
    if nuns[contem] == 9:
        nove += 1
    if nuns[contem] == 3:
        tres = 1
    if nuns[contem] % 2 == 0:
        par += 1
    if contem == 3:
        break
    contem += 1
print(f'vc digitou {nove} noves\nvc digitou {tres} tres\ne tem {par} numeros pares')

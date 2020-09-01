from random import randint
from time import sleep
conta = 0
pc = randint(0, 10)
print('=' * 56)
print('=-' * 8, end=' ')
print('TENTE ACERTAR O NUMERO', end=' ')
print('=-'*8)
print('=' * 56)
print('eu (o computador), vai pensar em um numero, entre 0 e 10, e vc vai ter q acertar!')
sleep(2)
jogador = int(input('qual e o seu palpite :'))
if jogador == pc:
    print('PARABENS, vc acertou de primeira!!')
else:
    while jogador != pc:
        conta += 1
        if jogador < pc:
            print('mais... tente mais uma vez')
            sleep(0.3)
        else:
            print('menos... tente mais uma vez')
            sleep(0.3)
        jogador = int(input('qual e o seu palpite :'))
    print('PARABENS, vc acertou em {} tentativas!'.format(conta+1))

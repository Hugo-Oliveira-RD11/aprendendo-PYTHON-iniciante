import random
from time import sleep
print('vamos jogar jokenpo!')
print('''escolha
[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura''')
escolha = int(input('qual vc vai escolher ?'))

if escolha == 1 or escolha == 2 or escolha == 3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔÔÔÔÔÔ!!!!')

    ale = random.randint(1,3)
    if escolha == 1:
        print('player escolheu PEDRA')
        if ale == 1:
            print('=' * 27)
            print('computador escolheu PEDRA')
            print('=' * 27)
            print('EMPATOU')
        elif ale == 2:
            print('=' * 27)
            print('computador escolheu PAPEL')
            print('=' * 27)
            print('VC PERDEU')
        elif ale == 3:
            print('=' * 27)
            print('computador escolheu TESOURA')
            print('=' * 27)
            print('VC GANHOU')
    elif escolha == 2:
        print('player escolheu PAPEL')
        if ale == 1:
            print('=' * 27)
            print('computador escolheu PEDRA')
            print('=' * 27)
            print('VC GANHOU')
        elif ale == 2:
            print('=' * 27)
            print('computador escolheu PAPEL')
            print('=' * 27)
            print('IMPATE')
        elif ale == 3:
            print('=' * 27)
            print('computador escolheu TESOURA')
            print('=' * 27)
            print('VC PEDEU')
    elif escolha == 3:
        print('player escolheu TESOURA')
        if ale == 1:
            print('=' * 27)
            print('computador escolheu PEDRA ')
            print('=' * 27)
            print('VC PERDEU')
        elif ale == 2:
            print('=' * 27)
            print('computador escolheu PAPEL')
            print('=' * 27)
            print('VC GANHOU')
        elif ale == 3:
            print('=' * 27)
            print('computador escolheu TESOURA')
            print('=' * 27)
            print('EMPATE')
else:
    print('OPÇÃO INVALIDA,reinicie o game, e digite um numero dentro das opções')

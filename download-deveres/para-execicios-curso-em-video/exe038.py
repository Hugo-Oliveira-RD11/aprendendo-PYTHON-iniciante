numero1 = int(input('digite um valor inteiro :'))
numero2 = int(input('digite outro valor :'))

if numero1 > numero2:
    maior = numero1
    print('o maior numero entre {} e {};\ne {}'.format(numero1, numero2, maior))

elif numero2 > numero1:
    maior = numero2
    print('o maior numero entre {} e {};\ne {}'.format(numero1, numero2, maior))

else:
    print('não existe maior numero!!, os dois são iguais')

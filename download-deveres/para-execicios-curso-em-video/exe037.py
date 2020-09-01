numero = int(input('digite um numero inteiro :'))
print('''escolhar um numero para a converçao 
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
escolha = int(input('digite um dos numeros dentro das opções :'))

if escolha == 1:
    print('A BINARIA do numero {} e {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O OCTANAL do numero {} e {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O hexadecimal do numero {} e {}',format(numero, hex(numero)[2:]))
else:
    print('por favor, DIGITE UM NUMERO DENTRO DAS OPÇOES!!')

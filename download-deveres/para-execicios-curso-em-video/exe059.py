from time import sleep
escolha = 0
n1 = int(input('primeiro valor :'))
n2 = int(input('segundo valor :'))
while escolha != 7:
    sleep(2)
    print('=-=' * 10)
    print('''VC QUER FAZER OQ COM ESSE NUMEROS ?
    [ 1 ] SOMA
    [ 2 ] SUBTRAIR
    [ 3 ] MULTIPLICAR
    [ 4 ] DIVIDIR
    [ 5 ] MAIOR NUMERO
    [ 6 ] NOVOS NUMEROS
    [ 7 ] SAIR''')
    escolha = int(input('qual e a sua escolha ?'))
    print('=-=' * 10)

    if escolha == 1:
        soma = n1 + n2
        sleep(0.3)
        print('o resultado de {} + {} é = {}'.format(n1, n2, soma))
    elif escolha == 2:
        subtrair = n1 - n2
        sleep(0.3)
        print('o resultado de {} - {} é = {}'.format(n1, n2, subtrair))
    elif escolha == 3:
        multplicar = n1 * n2
        sleep(0.3)
        print('o resultado de {} * {} é {}'.format(n1, n2, multplicar))
    elif escolha == 4:
        dividir = n1 / n2
        sleep(0.3)
        print('o resultado de {} / {} é {}'.format(n1, n2, dividir))
    elif escolha == 5:
        if n1 > n2:
            sleep(0.3)
            print('o maior entre {} e {} é {}'.format(n1, n2, n1))
        elif n2 > n1:
            sleep(0.3)
            print('o maior entre {} e {} é {}'.format(n1, n2, n2))
        elif n2 == n1:
            sleep(0.3)
            print('os dois numeros sao iguais!')
    elif escolha == 6:
        n1 = int(input('primeiro valor :'))
        n2 = int(input('segundo valor :'))
    else:
        print('por favor digite um numero dentro das opçoes!!')
print('finalizando...')
sleep(2)
print('fim do programa, volte sempre!.')

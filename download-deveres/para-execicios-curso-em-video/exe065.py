opcao = 's'
soma1 = 0
maior = 0
menor = 0
conta = 0
soma2 = 0
while opcao == 's':
    conta += 1
    n1 = int(input('digite um valor :'))
    if n1 == n1:
        soma1 += 1
        soma2 = soma2 + n1
        media = soma2 / soma1
    if conta == 1:
        maior = n1
        menor = n1
    elif conta != 1:
        if n1 > maior:
            maior = n1
        elif n1 < menor:
            menor = n1
    opcao = str(input('que continuar ? [ S / N ]')).lower()
print('''vc digitou {} numeros, a media entre eles e {:.2f}\no maior valor e {} e o menor valor e {}
'''.format(soma1, media, maior, menor))
